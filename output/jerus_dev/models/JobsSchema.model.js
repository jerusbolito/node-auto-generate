const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const JobsSchema = new Schema({
jobDescription:String,
jobCode:Number,
});

module.exports = mongoose.model("JobsSchema", JobsSchema);