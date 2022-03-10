import * as elasticsearch from "elasticsearch";

const ES_HOST = process.env.ES_HOST;

const esClient = new elasticsearch.Client({
  host: ES_HOST,
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
