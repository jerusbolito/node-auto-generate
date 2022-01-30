const router = require("express").Router();
const controller = require('../controllers/UsersSchema.controller.js');

router.get("/", controller.getAllDocuments);
router.post("/", controller.createDocument);

module.exports = router;