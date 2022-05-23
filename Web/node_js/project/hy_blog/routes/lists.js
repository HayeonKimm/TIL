const express = require("express");
const router = express.Router();

const Lists = require("../schemas/list");





const lists = [
    {
      title: "모두 들어라",
      name: "김하연1",
      data: 20220523
    },
    {

        title: "여러분.",
        name: "김하연2",
        data: 20220523

    },
    {
        title: "헬로",
        name: "김하연3",
        data: 20220523
    },
    {

      title: "헬로스3",
      name: "김하연4",
      data: 20220523
    },
];



// 데이터가 뜨는지 확인용

router.get("/lists",( req, res) => {

    res.json({
        lists
    });

});


// 타이틀로 목록 조회

router.get("/lists/:title", (req, res)=>{

    const title = req.params.title;


    res.json({


        detail: lists.filter((item)=>{

            return item.title === title;

        })[0],

    });

});


// 작성자명으로 조회 

router.get("/lists/:name", (req, res)=>{

    const name = req.params.name;


    res.json({


        detail: lists.filter((item)=>{

            return item.name === name;

        })[0],

    });

});

// 작성 날짜로 조회

router.get("/lists/:data", (req, res)=>{

    const date = req.params.data;


    res.json({


        detail: lists.filter((item)=>{

            return item.date === date;

        })[0],

    });

});





// 중복 게시물 검사 (Validation)

router.post("/lists", async (req, res) => {
	const { title, name, date } = req.body;

  const lists = await Lists.find({ title });

    // console.log(lists);

  if (lists.length) {
    return res.status(400).json({ success: false, errorMessage: "이미 있는 데이터입니다." });
  }

  const createdLists = await Lists.create({ title, name, date });

  res.json({ lists: createdLists });
  


});





// 2. 게시글 작성 API
//     - 제목, 작성자명, 비밀번호, 작성 내용을 입력하기'




// 3. 게시글 조회 API
//     - 제목, 작성자명, 작성 날짜, 작성 내용을 조회하기 
//     (검색 기능이 아닙니다. 간단한 게시글 조회만 구현해주세요.)
// 4. 게시글 수정 API
//     - API를 호출할 때 입력된 비밀번호를 비교하여 동일할 때만 글이 수정되게 하기
// 5. 게시글 삭제 API
//     - API를 호출할 때 입력된 비밀번호를 비교하여 동일할 때만 글이 삭제되게 하기


module.exports = router;