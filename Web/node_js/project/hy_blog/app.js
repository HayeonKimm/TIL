const express = require("express");
const req = require("express/lib/request");
const connect = require("./schemas");

const port = 3000;
const app = express();
const router = express.Router();

const listsRouter = require("./routes/lists");





app.use("/api", express.json(), [router,listsRouter]);


app.get("/", (req, res) => {
    res.send("Hi!");
  });



// 게시글 작성 API

// router.post('/list', (req, res) =>{


// });


//상품 상세 조회 API
router.get("/goods/:goodsId", (req, res) => {
	const { goodsId } = req.params;
	const [detail] = goods.filter((goods) => goods.goodsId === Number(goodsId));
	res.json({ detail });
});



app.listen(port, () => {
  console.log("서버가 켜졌어요!");
});