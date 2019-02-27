var express = require('express');
var router = express.Router();
const bodyParser = require("body-parser");
var cmd = require('node-cmd');

router.post('/', function(req, res, next){
  var filename;
  var pyProcess = cmd.get('cd ' + __dirname + ' && python ' + req.body.filetype + 'Test.py ' + req.body.filesize,
              function(data, err, stderr) {
                if (!err) {
                  console.log("data from python script " + data);
                } else {
                  filename = err;
                  var file = __dirname + '/' + filename.trim();
                  console.log("filename " + filename, file);
                  // var file = __dirname + '/' + filename.trim();
                  res.download(file); // Set disposition and send it.
                  }
              });
});


module.exports = router;
