import * as elasticsearch from "@elastic/elasticsearch";
import * as dotenv from "dotenv"

const vars = dotenv.config()
console.log('vars', vars)

const { ES_HOST } = vars.parsed;

console.log(`ES_HOST: ${ES_HOST}`);

const esClient = new elasticsearch.Client({
  node: ES_HOST,
  log: "error",
});

const getSensorData = async () => {
  console.log("in getSensorData");

  try {
    await esClient.ping(null);
    console.log("Ping ElasticSearch: Success");
  } catch (e) {
    console.log("Ping ElasticSearch: Error: ", e);
    return null;
  }
};

getSensorData();