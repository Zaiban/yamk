import { differenceInSeconds } from "date-fns";
import * as elasticsearch from "@elastic/elasticsearch";
import * as dotenv from "dotenv";

const vars = dotenv.config();
console.log("vars", vars);

const { ES_HOST, DEV_EUI } = vars.parsed;

const beginTime = "2019-02-19T00:00:00";
const endTime = "2019-03-19T23:59:59";

console.log(`ES_HOST: ${ES_HOST}`);

const esClient = new elasticsearch.Client({
  node: ES_HOST,
  log: "error",
});

const PULSEMETER_MULTIPLIER = 10;

const absPulseToPower = (time, pulseAbs, previous) => {
  const timeDiff = differenceInSeconds(new Date(time), new Date(previous.time));

  const pulseDiff = pulseAbs - previous.pulse1abs;
  const powerMultiplier = 3600 / timeDiff;

  return pulseDiff * powerMultiplier * PULSEMETER_MULTIPLIER;
};

export const pulseToPower = (pulse) => {
  return pulse * 12 * PULSEMETER_MULTIPLIER;
};

const getSensorData = async () => {
  console.log("in getSensorData");

  try {
    await esClient.ping(null);
    console.log("Ping ElasticSearch: Success");
  } catch (e) {
    console.log("Ping ElasticSearch: Error: ", e);
    return null;
  }

  const devEUIds = JSON.parse(DEV_EUI);

  for (const devEUI of devEUIds) {
    const DATAFIELD_KEY = `Dev_${devEUI}`;
    console.log("Looping: ", DATAFIELD_KEY);

    const response = await esClient.search({
      index: "logstash*",
      sort: "@timestamp:asc",
      body: {
        query: {
          bool: {
            must: [
              {
                range: {
                  "@timestamp": {
                    gte: beginTime,
                    lte: endTime,
                  },
                },
              },
              {
                match: {
                  "DevEUI_uplink.DevEUI": devEUI,
                },
              },
            ],
            //filter: filter.length > 0 ? filter : undefined,
          },
        },
        _source: [DATAFIELD_KEY, "@timestamp"],
        size: 10000,
      },
    });
    const { hits } = response.hits;

    const data = hits
      .map((hit, index) => {
        // Check that field exists
        if (typeof hit._source[DATAFIELD_KEY] === "undefined") return undefined;

        // Current values
        const time = hit._source["@timestamp"];
        const { pulse1, pulse1abs, ...rest } = hit._source[DATAFIELD_KEY];

        // Previous values
        const previous = { time: null, pulse1abs: null };
        if (
          typeof hits[index + 1] !== "undefined" &&
          hits[index + 1]._source[DATAFIELD_KEY].pulse1abs
        ) {
          previous.time = hits[index + 1]._source["@timestamp"];
          previous.pulse1abs = hits[index + 1]._source[DATAFIELD_KEY].pulse1abs;
        }

        // Parse power reading
        let power;
        if (pulse1abs === 0) {
          power = 0;
        } else if (previous.pulse1abs && pulse1abs) {
          power = absPulseToPower(time, pulse1abs, previous);
        } else if (pulse1) {
          power = pulseToPower(pulse1);
        }
        console.log("power", power);

        return {
          time,
          pulse1,
          pulse1abs,
          ...rest,
          power,
        };
      })
      .filter((item) => typeof item !== "undefined");

    //console.log("data", data);
    console.log("first", data[0]?.time);
    console.log("last", data[data.length - 1]?.time);
    console.log("size:", hits.length);
  }
};

getSensorData();
