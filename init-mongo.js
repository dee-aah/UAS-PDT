rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo_perpus:27017" },
    { _id: 1, host: "mongo_perpus_secondary:27017" }
  ]
})
