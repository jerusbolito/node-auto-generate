const UsersSchema = require('../models/UsersSchema.js');

exports.getAllDocuments = (req, res) => {
     UsersSchema.find({}, function(err, doc){
         if(err){
             res.status(500).json({status: 500, error: "Internal server error"});
         }else{
             res.status(200).json({status: 200, results: doc});
         }
     });
}

exports.createDocument = (req, res) => {
    let newDoc = new UsersSchema(req.body);

    newDoc.save(function(err, doc){
        if(err){
             res.status(500).json({status: 500, error: "Internal server error"});
         }else{
             res.status(200).json({status: 200, message: "Successfully created new item", results: doc});
         }
    });
}