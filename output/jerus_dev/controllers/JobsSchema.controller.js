const JobsSchema = require('../models/JobsSchema.js');

exports.getAllDocuments = (req, res) => {
     JobsSchema.find({}, function(err, doc){
         if(err){
             res.status(500).json({status: 500, error: "Internal server error"});
         }else{
             res.status(200).json({status: 200, results: doc});
         }
     });
}

exports.createDocument = (req, res) => {
    let newDoc = new JobsSchema(req.body);

    newDoc.save(function(err, doc){
        if(err){
             res.status(500).json({status: 500, error: "Internal server error"});
         }else{
             res.status(200).json({status: 200, message: "Successfully created new item", results: doc});
         }
    });
}