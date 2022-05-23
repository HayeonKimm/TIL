const express = require("express");
const router = express.Router();


router.get("/",( req, res) => {

    res.send("this is root page");

});

router.get("/list", (req,res) =>{


    res.send("this is list page");
});



module.exports = router;