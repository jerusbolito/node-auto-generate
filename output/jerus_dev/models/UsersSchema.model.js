const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const UsersSchema = new Schema({
username:String,
password:String,
});

module.exports = mongoose.model("UsersSchema", UsersSchema);