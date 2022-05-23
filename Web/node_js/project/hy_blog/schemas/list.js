const mongoose = require("mongoose");

const listsSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    unique: false
  },
  name: {
    type: String,
    required: true,
    unique: true
  },
  date: {
    type: String,
    required: true,
    unique: false
  },

});

module.exports = mongoose.model("Lists", listsSchema);