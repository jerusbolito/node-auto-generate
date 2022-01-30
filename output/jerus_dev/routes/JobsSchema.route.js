const router = require("express").Router();
const controller = require('../controllers/JobsSchema.controller.js');

router.get("/", controller.getAllDocuments);
router.post("/", controller.createDocument);

module.exports = router;