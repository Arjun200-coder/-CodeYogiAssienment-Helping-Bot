assignment_data = {
    "4.1": {
        "html": "<h1>Welcome to codeyogi</h1>",
        "css": "Empty",
        "js": "Empty"
    },

    "6.1": {
        "html": "<a href=" " target=" ">Click here</a> ",
        "css": "Empty",
        "js": "Empty"
    },
    
    "7.1": {
        "html": " <img src=" " alt=" "/> ",
        "css": "Empty ",
        "js": "Empty"
    },

    "8.1": {
        "html": "<h1>Welcome To Code Yogi</h1> <p>free software engineering training for underprivileged youths </p> ",
        "css": " h1{font-size: 40px; background: yellow; color: green; }, p{background: yellow;color: red;} ",
        "js": "Empty "
    },

    "10.1": {
        "html": " <div><h1>welcome to <span>codeyogi</span></h1> <h2>visit our<a href=" " target=" ">YouTube</a>channel</h2> <h2>connect with us:</h2> <a href=" " target=" ">twitter</a> <a href=" " target=" ">Linkedin</a> <a href=" " target=" ">Instagram</a></div> ",
        "css": " h1 {font-size: 40px; color: black; background: red; }, h2 {font-size: 30px; color: black; background: red; }, span {color: green; }, div{background: yellow;} ",
        "js": "Empty"
    },

    "11.1": {
        "html": " <h1>I want to learn Web Development ?</h1> <a href=" "target=" ">click here</a>",
        "css": "h1{font-size: 40px; margin-left: 10px; }, a{text-decoration: none; font-size: 20px; background: red; color: white; border: 4px dashed darkred; padding:10px 40px; margin-left: 10px; display: inline-block;}",
        "js": "Empty"
    },

    "12.1": {
        "html": " <div> <h1>notice board</h1></div> ",
        "css": "*{text-decoration: none; margin: 0; padding: 0; text-align: center;} div{margin: 10px; height: 500px; background: green; border: 16px solid black;} h1{font-size: 40px; padding: 4px 5px; border: 6px dotted black; margin-top: 30px; display: inline-block;} ",
        "js": "Empty"
    },

    "14.1": {
        "html": """ <div> <h1>Heading 1</h1> <p>Paragraph 1</p> <p>Paragraph 2</p> <p>Paragraph 3</p> <p>Paragraph 4</p> </div>""",
        "css": """
                div { background: yellow; }
                h1 { background: yellow; font-size: 60px; color: blue; }
                p { background: yellow; color: green; font-size: 40px; }
                """,
        "js": "Empty"
    },

    "18.1": {
        "html": """ <div class="header"><div class="link"><a href=" ">HOME</a><a href=" ">ABOUT</a><a href=" ">COURSES</a><a href=" ">CONTACT</a></div></div><div class="main"><h1>welcome to codeyogi</h1> <p>Join our <a href="">React</a> Batch</p> <p>Join our <a href="">Node.js</a> Batch</p> <p>Join our <a href="">Machine Learning </a>Batch</p> <p>Our other batches:</p> <a class="box" href="">Html</a> <a class="box" href="">Css</a> <a class="box" href="">javascpit</a> <a class="box" href="">python</a> </div> <div class="footer"><div class="ram"><div class="ra"> <a href="">Facebook</a> <a href="">Twitter</a> <a href="">linkedin</a> <a href="">Instagram</a> </div> </div> </div>""",
        "css": """
* {
margin: 0;
padding: 0;
text-decoration: none;
}

.header {
padding: 20px;
background: black;
}

.box {
border: 2px solid green;
padding: 3px;
border-radius: 10px;
margin: 0;
}

a {
color: green;
}

.footer {
background: yellow;
height: 20px;
padding: 20px;
margin-top: 350px;
text-align: right;
}

.link,
.ram {
border: 4px solid green;
padding: 4px 5px;
display: inline-block;
}

a + a {
margin-left: 10px;
}

h1 {
margin: 30px 0;
font-size: 40px;
}

p {
margin: 15px 0;
font-size: 20px;
}

.main {
min-height: calc(-152px + 100vh);
margin-left: 15px;
box-sizing: border-box;
}
""",
        "js": "Empty"
    },

    "18.2": {
        "html": """
<img src="https://codeyogi.io/student.jpg" />
<h1>Hey, I am Matt Farley</h1>
<h2>Web Designer and Developer</h2>
<p>design and code beautifully simple things,and I love what I do.</p>
<h6>Lets connect with me:</h6>
<a href=""> Instagram</a>
<a href="">Facebook</a>
<a href="">Twitter</a>
<a href="">Linkedin</a>
""",
        "css": """ .h1 { font-size: 60px; } h6 { display: inline-block; } a { border: 4px solid green; text-decoration: none; color: green; padding: 2px; margin-right: 3px; border-radius: 10px; } """,
        "js": "Empty"
    },

    "19.1": {
        "html": """
<div id="header">
<div class="link-box">
    <a href="">HOME</a>
    <a href="">ABOUT</a>
    <a href="">COURSES</a>
    <a href="">CONTACT US</a>
</div>
</div>
<div id="main">
<h1 class="mainheading">Welcome To CodeYogi</h1>
<p>Join our <a href="">React</a> Batch</p>
<p>Join our <a href="">Node.js</a> Batch</p>
<p>Join our <a href="">Machine Learning</a> Batch</p>
<p>Our other batches:</p>
<a href="" class="other-course">HTML</a>
<a href="" class="other-course">CSS</a>
<a href="" class="other-course">JavaScript</a>
<a href="" class="other-course">Python</a>
</div>
<div id="footer">
<div class="link-box">
    <a href="">FACEBOOK</a>
    <a href="">INSTAGRAM</a>
    <a href="">LINKEDIN</a>
    <a href="">TWITTER</a>
</div>
</div>
""",
        "css": """
* {
margin: 0;
padding: 0;
text-decoration: none;
}

a {
color: green;
}

#header {
background: black;
}

#footer {
background: yellow;
text-align: right;
background-image: url("https://codeyogi.io/footer.jpg");
}

#header a + a,
#footer a + a {
margin-left: 30px;
}

.link-box {
border: 4px solid green;
display: inline-block;
padding: 5px;
}

#header,
#footer {
padding: 20px;
}

#main {
padding: 60px 0px 60px 20px;
min-height: calc(100vh - 152px);
box-sizing: border-box;
background: url("https://codeyogi.io/coffee.jpg") no-repeat right center/cover;
}

h1 {
font-size: 80px;
}

.mainheading {
margin-bottom: 60px;
}

p {
font-size: 40px;
}

p + p {
margin-top: 10px;
}

.other-course {
border: 2px solid green;
padding: 14px;
display: inline-block;
border-radius: 10px;
}
""",
        "js": "Empty"
    },


    "20.1": {
        "html": """
<div id="header">
<div class="link-box">
    <a href="">HOME</a>
    <a href="">ABOUT</a>
    <a href="">COURSES</a>
    <a class="bold" href="">CONTACT US</a>
</div>
</div>
<div id="main">
<h1 class="mainheading">Welcome To CodeYogi</h1>
<p>Join our <a href="">React</a> Batch</p>
<p>Join our <a href="">Node.js</a> Batch</p>
<p>Join our <a href="">Machine Learning</a> Batch</p>
<p>Our other batches:</p>
<a href="" class="other-course">HTML</a>
<a href="" class="other-course">CSS</a>
<a href="" class="other-course">JavaScript</a>
<a href="" class="other-course">Python</a>
</div>
<div id="footer">
<div class="link-box">
    <a href="">FACEBOOK</a>
    <a href="">INSTAGRAM</a>
    <a href="">LINKEDIN</a>
    <a href="">TWITTER</a>
</div>
</div>
""",
        "css": """
* {
margin: 0;
padding: 0;
text-decoration: none;
}

.bold {
font-weight: bold;
}

.main > a {
font-family: "caveat", cursive;
}

a {
color: green;
text-decoration: none;
}

#header {
background: black;
}

#footer {
background: yellow;
text-align: right;
background: url("https://codeyogi.io/footer.jpg");
}

#header a + a,
#footer a + a {
margin-left: 30px;
font-family: "caveat", cursive;
}

.link-box {
border: 4px solid green;
display: inline-block;
padding: 5px;
}

#header,
#footer {
padding: 20px;
font-family: "caveat", cursive;
}

#main {
padding: 60px 0px 60px 20px;
min-height: calc(100vh - 152px);
box-sizing: border-box;
background: url("https://codeyogi.io/coffee.jpg") no-repeat right center /
    cover;
}

h1 {
font-size: 80px;
font-family: "caveat", cursive;
}

.mainheading {
margin-bottom: 60px;
}

p {
font-size: 40px;
font-family: "caveat", cursive;
}

p + p {
margin-top: 10px;
}

.other-course {
border: 2px solid green;
padding: 14px;
display: inline-block;
border-radius: 10px;
}
""",
        "js": "Empty"
    },


    "21.1": {
        "html": """
<div id="header">
  <div class="link-box">
    <a href="">HOME</a>
    <a href="">ABOUT</a>
    <a href="">COURSES</a>
    <a href="" class="focus">CONTACT US</a>
  </div>
</div>
<div id="main">
  <h1 class="mainheading">Welcome To CodeYogi</h1>
  <p>Join our <a href="">React</a> Batch</p>
  <p>Join our <a href="">Node.js</a> Batch</p>
  <p>Join our <a href="">Machine Learning</a> Batch</p>
  <p>Our other batches:</p>
  <a href="" class="other-course">HTML</a>
  <a href="" class="other-course">CSS</a>
  <a href="" class="other-course">JavaScript</a>
  <a href="" class="other-course">Python</a>
</div>
<div id="footer">
  <div class="link-box">
    <a href="">FACEBOOK</a>
    <a href="">INSTAGRAM</a>
    <a href="">LINKEDIN</a>
    <a href="">TWITTER</a>
  </div>
</div>
""",
       "css": """
* {
  margin: 0;
  padding: 0;
  text-decoration: none;
}

a {
  color: rgb(51, 204, 51);
}

#header {
  background: black;
}

#footer {
  background: url("https://codeyogi.io/footer.jpg");
  text-align: right;
}

#header a + a,
#footer a + a {
  margin-left: 30px;
}

.link-box {
  border: 4px solid rgb(51, 204, 51);
  display: inline-block;
  padding: 5px;
}

#header,
#footer {
  padding: 20px;
}

#main {
  padding: 60px 0px 60px 20px;
  min-height: calc(100vh - 152px);
  box-sizing: border-box;
  background: url("https://codeyogi.io/coffee.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: right center;
}

h1 {
  font-size: 80px;
  font-family:"Dancing Script", cursive;
}

.mainheading {
  margin-bottom: 60px;
}

p {
  font-size: 40px;
  font-family: "Dancing Script", cursive;
}

p + p {
  margin-top: 10px;
}

.other-course {
  border: 2px solid rgb(51, 204, 51);
  padding: 14px;
  display: inline-block;
  border-radius: 10px;
}

#header a {
  font-family: Tahoma, Verdana, sans-serif;
}

.focus {
  font-weight: bold;
}
""",
        "js": "Empty"
    },


    "22.1": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: flex-start;
  flex-direction: column;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },


    "22.2": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
       "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: flex-end;
  justify-content: center;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },

    "22.3": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-end;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },


    "22.4": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
       "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: flex-end;
  flex-direction: column;
  justify-content: center;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },

    "22.5": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: center;
  justify-content: space-between;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },


    "22.6": {
        "html": """
<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
  <p>4</p>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  display: flex;
  background: green;
  height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: space-evenly;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },


    "22.7": {
        "html": """
<div>
  <h1>CodeYogi</h1>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

div {
  background: green;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

h1 {
  font-size: 60px;
}
""",
        "js": """ Empty"""
    },


    "22.8": {
        "html": """
<div id="main">
  <div class="up">
    <p>1</p>
    <p>2</p>
  </div>
  <div class="down">
    <p>3</p>
    <p>4</p>
  </div>
</div>
 
""",
       "css": """
* {
  padding: 0;
  margin: 0;
}

#main {
  display: flex;
  background: green;
  height: 100vh;
  flex-direction: column;
  justify-content: space-between;
}

.up {
  display: flex;
  justify-content: space-between;
}

.down {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}
""",
        "js": "Empty"
    },


    "22.9": {
       "html": """
<div id="main">
  <div id="up">
    <p>1</p>
  </div>

  <div id="beech">
    <p>2</p>
  </div>

  <div id="end">
    <p>3</p>
  </div>
</div>
   
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

#main {
  display: flex;
  background: green;
  height: 100vh;
  justify-content: space-between;
  flex-direction: column;
}

div > div {
  display: flex;
}

#end {
  justify-content: flex-end;
}

#beech {
  justify-content: center;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}

#up {
  justify-content: flex-start;
}
""",
        "js": "Empty"
    },

    "22.10": {
        "html": """
<div id="main">
  <div class="one">
    <p>1</p>
  </div>

  <div class="two">
    <p>2</p>
    <p>3</p>
  </div>

  <div class="one">
    <p>4</p>
  </div>
</div>
""",
        "css": """
* {
  padding: 0;
  margin: 0;
}

#main {
  display: flex;
  background: green;
  height: 100vh;
  flex-direction: column;
  justify-content: space-between;
}

p {
  padding: 15px 20px;
  background: yellow;
  border: 5px solid red;
}

.one {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

div .two {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}
""",
        "js": "Empty"
    },

    "23.1": {
        "html": """
<div id="container">
  <div id="header">
    <div>
      <a href="">HOME</a>
      <a href="">ABOUT</a>
      <a href="">COURSES</a>
      <a href="">CONTACT US</a>
    </div>
    <button>Sign up</button>
  </div>

  <div id="main">
    <img src="https:\codeyogi.io\logo.png" alt="logo" />
    <h1>Codeyogi</h1>
  </div>

  <div id="footer">
    <a href="">FACEBOOK</a>
    <a href="">INSTAGRAM</a>
    <a href="">LINKEDIN</a>
    <a href="">TWITTER</a>
  </div>
</div>
""",
       "css": """
#container {
  min-height: 400px;
  display: flex;
  flex-direction: column;
}

* {
  margin: 0;
  padding: 0;
  text-decoration: none;
}

a {
  color: rgb(51, 204, 51);
}

#header {
  background: black;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

#footer {
  background: yellow;
  display: flex;
  justify-content: flex-end;
}

#header a + a,
#footer a + a {
  margin-left: 30px;
}

#header,
#footer {
  padding: 20px;
}

#main {
  padding: 60px 0px 60px 20px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
  flex-direction: column;
  min-height: 100vh;
}

#header a {
  font-family: Tahoma, Verdana, sans-serif;
}

button {
  background: rgb(51, 204, 51);
  padding: 8px 10px;
  font-size: 25px;
  border-radius: 8px;
}
""",
        "js": "Empty"
    },

    "23.2": {
        "html": """
<div class="main">
  <img
    src="https://codeyogi.io/html_css.jpg"
    alt="codeyogi"
    style="width: 100%"
  />
  <p>HTML & CSS</p>

  <h2>
    The company itself is a very successful company. The same reason follows,
    our choice of pleasures something pain for, no one escapes these loose, do
    not know the pleasures of the body? We will never forgive her. Right?
  </h2>

  <div id="link">
    <a href="">Read more</a>
  </div>
</div>
""",
        "css": """
* {
  margin: 0;
  padding: 0;
  text-decoration: none;
}

.main {
  border: 5px solid black;
  color: white;
  background: gray;
  display: flex;
  flex-direction: column;
  min-width: 300px;
  margin: 15px;
  padding: 10px;
}

#link {
  display: flex;
  justify-content: center;
}

a {
  margin: 5px;
  display: inline-block;
  background: rgb(12, 242, 39);
  border: 2px solid rgb(12, 242, 39);
  color: white;
  border-radius: 99px;
  justify-content: center;
  padding: 0 10px;
}

p {
  display: flex;
  justify-content: center;
}

h2 {
  display: flex;
  padding: 6px;
}
""",
        "js": "Empty"
    },

    "23.4": {
        "html": """
<div class="header">
  <img style="width: 20px;" src="https://codeyogi.io/nike.png" />
  <div class="text">
    <a href="">Home</a>
    <a href="">Products</a>
    <a href="">Orders</a>
    <a href="">About us</a>
  </div>
</div>

<div class="powerful">
  <div class="babba">
    <div class="potta">
      <img style="max-width: 100%;" class="images" src="https://codeyogi.io/nike_1.jpg" />
    </div>
    <div class="detail">
      <h2>Nike Air Force 1</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, ratione
        consectetur, nostrum voluptates optio dolore aliquid nam, nemo fugit
        harum soluta iure nesciunt placeat corporis? Ea veniam numquam ducimus.
      </p>
      <button class="price">Price-87.99 S</button>
      <a href="">more details....</a>
    </div>
  </div>
  <div class="babba">
    <div class="potta">
      <img style="max-width: 100%;" class="images" src="https://codeyogi.io/nike_2.jpeg" />
    </div>
    <div class="detail">
      <h2>Nike Air Force 1</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, ratione
        consectetur, nostrum voluptates optio dolore aliquid nam, nemo fugit
        harum soluta iure nesciunt placeat corporis? Ea veniam numquam ducimus.
      </p>
      <button class="price">Price-87.99 S</button>
      <a href="">more details....</a>
    </div>
  </div>
  <div class="babba">
    <div class="potta">
      <img style="max-width: 100%;" class="images" src="https://codeyogi.io/nike_3.jpg" />
    </div>
    <div class="detail">
      <h2>Nike Air Force 1</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, ratione
        consectetur, nostrum voluptates optio dolore aliquid nam, nemo fugit
        harum soluta iure nesciunt placeat corporis? Ea veniam numquam ducimus.
      </p>
      <button class="price">Price-87.99 S</button>
      <a href="">more details....</a>
    </div>
  </div>
  <div class="babba">
    <div class="potta">
      <img style="max-width: 100%;" class="images" src="https://codeyogi.io/nike_4.jpg" />
    </div>
    <div class="detail">
      <h2>Nike Air Force 1</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, ratione
        consectetur, nostrum voluptates optio dolore aliquid nam, nemo fugit
        harum soluta iure nesciunt placeat corporis? Ea veniam numquam ducimus.
      </p>
      <button class="price">Price-87.99 S</button>
      <a href="">more details....</a>
    </div>
  </div>
</div>

<div class="footer">
  <p>find a store near you ?</p>
  <div class="fimage">
    <img src="https://codeyogi.io/youtube.png" />
    <img src="https://codeyogi.io/twitter.png" />
    <img src="https://codeyogi.io/instagram.png" />
    <img src="https://codeyogi.io/facebook.png" />
  </div>
  <div class="footer">
    <p>Need and help ?</p>
  </div>
</div>
""",
        "css": """* {
  margin: 0;
  padding: 0;
  text-decoration: none;
  box-sizing: border-box;
}

.header img {
  max-width: 40px;
}

.powerful {
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  background: green;
  justify-content: space-between;
  height: 50px;
  align-items: center;
}

.text a {
  color: black;
}

.text {
  display: flex;
  align-items: center;
  font-size: 20px;
  width: 40%;
  justify-content: space-between;
}

.images {
  max-width: 100%;
}

.potta {
  margin: 0 10px 0 0;
  width: 100%;
}

.image {
  display: flex;
  min-width: 0;
  max-width: 100%;
  margin: 10px;
}

h2 {
  margin: 10px 0;
  color: orange;
}

.detail p {
  font-size: 20px;
}

.babba {
  display: flex;
  margin: 6prsnt auto;
  border: 5px solid black;
  width: 799px;
  height: auto;
  align-items: center;
}

.footer img {
  max-width: 40px;
  justify-content: center;
  align-items: center; /* align-itemsenter typo fixed */
}

.footer {
  display: flex;
  height: 40px;
  justify-content: space-between;
  align-items: center;
  background: yellow;
}

button {
  border-radius: 5px;
  padding: 2px;
  color: orange;
  font-size: 12px;
  text-align: center;
  display: block;
}

@media (max-width: 600px) {
  .header {
    height: 20px;
  }

  .detail p {
    font-size: 3px;
  }

  .babba {
    max-width: 330px;
    border: 3px solid black;
  }

  .potta {
    width: 680px;
  }

  .text {
    font-size: 5px;
  }

  h2 {
    margin: 4px 0;
    font-size: 12px;
  }

  button {
    border-radius: 5px;
    padding: 1px;
    font-size: 3px;
  }

  .detail a {
    font-size: 3px;
  }

  .footer img {
    max-width: 20px;
  }

  .footer {
    height: 30px;
  }
}

@media (min-width: 600px) {
  .header {
    height: 40px;
  }

  .detail p {
    font-size: 15px;
  }

  .babba {
    max-width: 660px;
    border: 5px solid black;
  }

  .potta {
    width: 700px;
  }

  .text {
    font-size: 5px;
  }

  h2 {
    margin: 4px 0;
    font-size: 32px;
  }

  button {
    border-radius: 5px;
    padding: 1px;
    font-size: 3px;
  }

  .detail a {
    font-size: 10px;
  }

  .footer img {
    max-width: 30px;
  }

  .footer {
    height: 40px;
  }
}
 """,
        "js": "Empty"
    },

    "24.1": {
        "html": """ <div class="container">
 
  <div class="header">
    <div class="student-img">
      <img src="https://codeyogi.io/student.jpg" alt="student-image" />
    </div>
    <div class="content">
      <p>hey,</p>
      <h1>I'm matt farley</h1>
      <p>web designer and developer</p>
      <div class="social-icons">
        <img src="https://codeyogi.io/twitter.png" alt="twitter logo" />
        <img src="https://codeyogi.io/instagram.png" alt="instagram logo" />
        <img src="https://codeyogi.io/facebook.png" alt="Facebook logo" />
        <img src="https://codeyogi.io/linkedin.png" alt="linkedin logo" />
      </div>
    </div>
  </div>
  <div class="skills-heading">
    <h2>my skills</h2>
  </div>
  <div class="skills">
    <div class="skill">
      <img src="https://codeyogi.io/html.png" alt="html logo" />
      <p>html</p>
    </div>
    <div class="skill">
      <img src="https://codeyogi.io/css.png" alt="css logo" />
      <p>css</p>
    </div>
    <div class="skill">
      <img src="https://codeyogi.io/javascript.png" alt="JavaScript logo" />
      <p>JavaScript</p>
    </div>
  </div>
</div>""",
        "css": """* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
body {
  background: gray;
}
.container {
  padding: 40px;
  display: flex;
  flex-direction: column;
}
.header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}
.content {
  padding: 50px 50px 0 50px;
}
.content,
p,
h1 {
  margin: 10px;
}
.content p {
  color: #fff;
  font-size: 25px;
}
.content h1 {
  font-size: 65px;
  color: yellow;
}
.social-icons {
  margin-left: 20px;
  display: flex;
  gap: 10px;
  margin-top: 20px;
}
.social-icons img {
  width: 40px;
}
.skills-heading {
  background-color: #b0b0b0;
  margin: 60px 20px 20px 0;
  text-align: center;
}
.skills-heading h2 {
  color: yellow;
  font-size: 30px;
  padding: 2px 10px;
}
.skills {
  padding: 20px;
  align-items: center;
  font-size: 25px;
  display: flex;
  justify-content: space-around;
  margin-top: 50px;
}
.skill {
  display: inline-block;
  margin: 10px;
}
.skill img {
  height: 200px;
  width: 180px;
}
.skill p {
  margin: 10px 0;
} """,
        "js": "Empty"
    },

    "25.1": {
        "html": """ <h1>Media Queries</h1> """,
        "css": """h1 {
  color: initial;
}
@media (max-width: 640px) {
  h1 {
    color: red;
  }
}
@media (min-width: 641px) and (max-width: 767px) {
  h1 {
    color: green;
  }
}
@media (min-width: 768px) and (max-width: 1023px) {
  h1 {
    color: blue;
  }
}
@media (min-width: 1024px) {
  h1 {
    color: yellow;
  }
} 
 """,
        "js": "Empty"
    },

    "25.2": {
        "html": """<div>
  <p>1</p>
  <p>2</p>
  <p>3</p>
</div> """,
        "css": """* {
  padding: 0;
  margin: 0;
}

p {
  background: red;
  padding: 8px;
  border: 2px blue solid;
}

div {
  height: 100vh;
  background: green;
  flex-direction: row;
}

@media (orientation: portrait) {
  div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }
}

@media (orientation: landscape) {
  div {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }
}
  """,
        "js": "Empty"
    },

    "27.1": {
        "html": """<div class="main">
  <div class="images">
    <img class="top" src="https://codeyogi.io/bag.jpg" />
    <div class="small">
      <img src="https://codeyogi.io/bag_1.jpg" />
      <img src="https://codeyogi.io/bag_2.jpg" />
      <img src="https://codeyogi.io/bag_3.jpg" />
      <img src="https://codeyogi.io/bag_4.jpg" />
    </div>
  </div>
  <div class="h1p">
    <h1>Zip Tote Basket</h1>
    <p>$140</p>
    <div>
      <img src="https://codeyogi.io/star.png" />
      <img src="https://codeyogi.io/star.png" />
      <img src="https://codeyogi.io/star.png" />
      <img src="https://codeyogi.io/star.png" />
      <img src="https://codeyogi.io/grey-star.png" />
    </div>
    <p class="detail">
      The Zip Tote Basket is the perfect midpoint between shopping tote and
      comfy backpack. With convertible straps, you can hand carry, shoulder sling,
      or backpack this convenient and spacious bag. The zip top and durable
      canvas construction keeps your goods protected for all-day use.
    </p>
    <button>Add to cart</button>
  </div>
</div>  """,
        "css": """ * {
  margin: 0px;
  padding: 0px;
  text-decoration: none;
}

.top {
  max-width: 100%;
  min-width: 0%;
}

.h1p {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  gap: 10px;
  padding: 25px 20px;
}

.h1p p {
  color: gray;
}

.main {
  display: flex;
  flex-direction: column;
  max-width: 1000px;
}

button {
  font-size: 20px;
  border: none;
  background: blue;
  color: white;
  padding: 5px 30px;
  align-self: center;
  border-radius: 5px;
}

h1,
p,
.detail {
  font-family: Tahoma, Geneva, Verdana, sans-serif;
}

.small {
  display: none;
}

.small img {
  min-width: 0%;
}

@media (min-width: 750px) {
  .main {
    flex-direction: row-reverse;
    border: 10px solid gray;
    padding: 20px;
    border-radius: 30px;
    margin: 20px auto;
  }

  button {
    align-self: flex-start;
  }

  .h1p {
    width: 60%;
  }

  .images {
    width: 40%;
  }

  .small {
    display: flex;
    gap: 5px;
    min-width: 0%;
  }

  .small img {
    min-width: 0%;
  }
}

@media (min-width: 900px) {
  h1 {
    font-size: 50px;
  }

  p {
    font-size: 25px;
  }

  button {
    font-size: 30px;
  }
}""",
        "js": "Emptyt"
    },

    "28.1": {
        "html": """ <div>
  <p id="p1">1</p>
  <p id="p2">2</p>
</div> """,
        "css": """* {
  padding: 0;
  margin: 0;
  text-decoration: none;
}

body {
  height: 200vh;
}

div {
  height: 70vh;
  background-color: green;
  margin: 40px;
}

p {
  font-size: 40px;
  color: white;
  text-align: center;
  padding: 30px 50px;
}

#p1 {
  background: blue;
}

#p2 {
  background: red;
  position: fixed;
  right: 0;
  bottom: 0;
  margin: 0;
}
  """,
        "js": "Empty"
    },

    "28.2": {
        "html": """ <div>
  <p id="p1">1</p>
  <p id="p2">2</p>
</div> """,
        "css": """* {
  padding: 0;
  margin: 0;
  text-decoration: none;
}

body {
  height: 200vh;
}

div {
  height: 70vh;
  background-color: green;
  margin: 40px;
}

p {
  font-size: 40px;
  color: white;
  text-align: center;
  padding: 30px 50px;
}

#p1 {
  background: red;
}

#p2 {
  background: blue;
  position: sticky;
  top: 0px;
  bottom: 40px;
}
  """,
        "js": "Empty"
    },

    "28.3": {
        "html": """ <div>
  <p id="p1">1</p>
  <p id="p2">2</p>
</div>  """,
        "css": """ * {
    padding: 0;
    margin: 0;
    text-decoration: none;
  }

  body {
    height: 200vh;
  }

  div {
    height: 70vh;
    background-color: green;
    margin: 40px;
  }

  p {
    font-size: 40px;
    color: white;
    text-align: center;
    padding: 30px 50px;
  }

  #p1 {
    background: red;
    position: relative;
    top: 50px;
  }

  #p2 {
    background: blue;
  } """,
        "js": "Empty"
    },

    "28.4": {
        "html": """ <div>
  <p id="p1">1</p>
  <p id="p2">2</p>
</div>  """,
        "css": """* {
    padding: 0;
    margin: 0;
    text-decoration: none;
  }

  body {
    height: 200vh;
  }

  div {
    height: 70vh;
    background-color: green;
    margin: 40px;
    position: relative;
  }

  p {
    font-size: 40px;
    color: white;
    text-align: center;
    padding: 30px 50px;
  }

  #p1 {
    background: red;
  }

  #p2 {
    background: blue;
    position:absolute;
    right: 0;
    bottom: 0;
  }  """,
        "js": "Empty"
    },

    "28.5""": {
        "html": """ <div id="sidebar">
  <p>S</p>
  <p>I</p>
  <p>D</p>
  <p>E</p>
  <p>B</p>
  <p>A</p>
  <p>R</p>
</div>
  <div id="content">
    <div>
      <h1>Paragraph 1</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
    <div>
      <h1>Paragraph 2</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
    <div>
      <h1>Paragraph 3</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
    <div>
      <h1>Paragraph 4</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
    <div>
      <h1>Paragraph 5</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
    <div>
      <h1>Paragraph 6</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sintoccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
        laborum. Sed ut
        perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
        eaque ipsa quaeabillo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
        voluptatem
        quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem
        sequi
        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
        nonnumquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
    </div>
</div>  """,
        "css": """ * {
  padding: 0;
  margin: 0;
}

#sidebar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 20px;
  background: green;
  color: white;
  align-items: center;
  width: 200px;
  position: fixed;
  top: 0;
  bottom: 0;
}

#sidebar > p,
h1 {
  font-size: 40px;
}

#content p {
  margin-top: 20px;
  font-size: 20px;
}

#content {
  display: flex;
  flex-direction: column;
  gap: 60px;
  padding: 60px;
  background: yellow;
  margin-left: 200px;
}
 """,
        "js": "Empty"
    },

    "29.1": {
        "html": """ <h1>
  Kaun kehta hai bachpan aasan tha. Kuch zimmeydariyaan tab bhi sambhalni
  padtithi 🤣
</h1>
<img src="https://codeyogi.io/bachpan.png" />
  """,
        "css": """ h1 {
  padding: 10px;
  width: 700px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  position: relative;
  z-index: 1;
}

img {
  width: 720px;
  margin-top: -120px;
}
 """,
        "js": "Empty "
    },

    "30.1": {
        "html": """ <div class="one">
  <h1>Coding sikhne ki sabse achi jagah?</h1>
  <div class="input">
    <div>
      <input type="radio" id="one" name="only" />
      <label for="one">Codeyogi</label>
    </div>
  
  <div>
      <input type="radio" id="two" name="only" />
      <label for="two">Saare bolo, Codeyogi</label>
    </div>
  </div>

  <div class="lable">
    <div>
      <input type="radio" id="three" name="only" />
      <label for="three">Jor se bolo, Codeyogi</label>
    </div>
    <div>
      <input type="radio" id="four" name="only" />
      <label for="four">Mummy kasam, Codeyogi</label>
    </div>
  </div>
  
  <div class="main">
    <button>Submit</button>
  </div>
</div>
  """,
        "css": """* {
  margin: 0;
  paddig: 0;
  text-decoration: none;
}

.one {
  background: rgb(51, 255, 245);
  border: 2px solid black;
  border-raduis: 10px;
  padding: 30px;
  max-width: 600px;
  margin: auto;
  margin-top: 50%;
  border-radius: 5px;
}

h1 {
  margin-bottom: 15px;
}

.main {
  display: flex;
  align-items: center;
  justify-content: center;
}

button {
  background: lightblue;
  padding: 0 20px;
  margin-top: 50px;
  margin-bottom: 1px;
  border-radius: 5px;
  display: block;
}

.input {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  Flex-direction: column;
  row-gap: 4px;
}

.lable {
  display: flex;
  justify-content: space-between;
  
}
  """,
        "js": "Empty"
    },

    "30.2": {
        "html": """ <form class="container">
  <div>
    <label for="one">name</label>
    <input
      type="text"
      id="one"
      placeholder="enter your name"
      name="one"
    /><br />
  </div>
  <div>
    <label for="two">Age</label>
    <input
      type="number"
      id="two"
      placeholder="enter your age"
      name="one"
    /><br />
  </div>
  <div>
    <label for="three">phone number </label>
    <input
      type="tel"
      id="three"
      placeholder="enter your phone number"
      name="one"
    /><br />
  </div>
  <div>
    <label for="four">email </label>
    <input
      type="email"
      name="one"
      id="four"
      placeholder="enter your email"
    /><br />
  </div>
  <div>
    <label for="four">email password</label>
    <input
      type="password"
      name="one"
      id="four"
      placeholder="enter your email password"
    /><br />
  </div>
  <div>
    <label name="one" for="five">Gender</label>
    <select placeholder="Gender" name="one">
      <option value="male">male</option>
      <option value="fimale">fimale</option>
      <option value="other">other</option></select
    ><br />
  </div>
  <div>
    <label for="six">Instagram profile </label>
    <input
      name="one"
      type="url"
      id="six"
      placeholder="enter link of your Instagram"
    /><br />
  </div>
  <div>
    <label for="seven"> favourite colour </label>
    <input  placeholder="color" type="color" name="one" id="seven" /><br />
  </div>
  <div>
    <label for="eight">Date of birth </label>
    <input type="date" name="one" id="eight" /><br />
  </div>
  <div>
    <label for="ten">time of birth </label>
    <input type="time" name="one" id="ten" /><br />
  </div>
  <div>
    <p class="one">Which type of person are you?</p>
    <input type="radio" id="eleven" name="only one" />
    <lable for="eleven">Introvert</lable>
    <input type="radio" id="eleven" name="only one" />
    <lable for="eleven">Extrovert</lable>
  </div>
  <div>
    <p class="two">How much percentage do you scored in class 10th ?</p>
    <input name="one" type="range" min="30" max="100" />
  </div>
  <div>
    <p id="hindu">What are your qualities?</p>
    <input type="checkbox" id="are" name="one" />
    <label for="are"> Sarkari naukari</label><br />
  </div>
  <div>
    <input type="checkbox" id="are" name="one" />
    <label for="are"> Handsome/Beautiful</label><br />
  </div>
  <div>
    <input type="checkbox" id="are" name="one" />
    <label for="are">Stylish hairs</label><br />
  </div>
  <div>
    <input type="checkbox" id="are" name="one" />
    <label for="are">Fair skin</label><br />
  </div>
  <div>
    <label for="is">upload your image <input type="file" id="is" name="one"/> </label>
  </div>
  <div>
    <p class="partner">what is your name of your girlfriend/boyfriend?</p>
    <input type="text" name="one" placeholder="enter your partner name" /><br />
  </div>
  <div><label for="for"> tell more about yourself </label><br /></div>
  <div><textarea>enter text here</textarea><br /></div>
  <div>
    <label for="nine"> Date an time of filling this form:</label>
    <input type="datetime-local" id="nine" name="one" /><br />
  </div>
</form>
  """,
        "css": """* {
  margin-bottom: 10px;
}

.container {
  display: flex;
  flex-direction: column;
  row-gap: 20px;
  column-gap: 20px;
  align-items: flex-start;
}
  """,
        "js": "Empty"
    },

    "31.1": {
        "html": """ <div class="grand">
  <div class="powerfull">
    <form action="https://codeyogi.io/save">
      <h1>join codeyogi</h1>
      <div class="up">
        <div class="main">
          <label for="name">your name</label>
          <input type="text" id="name" name="name" required />

          <label for="email"> your email</label>
          <input type="email" id="email" name="email" required />

          <label for="password">your password</label>
          <input type="password" id="password" name="password" required />

          <div class="signup">
            <button type="submit">signup</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>
  """,
        "css": """* {
  margin: 0;
  padding: 0;
}

.powerfull {
  border: 10px solid white;
  max-width: 220px;
  background: rgb(86, 87, 115);
  padding: 30px 50px;
  border-radius: 20px;
}

.grand {
  display: flex;
  justify-content: center;
  margin: 50prsnt auto;
  width: 220px;
}

.singup {
  text-align: center;
}

button {
  background: blue;
  padding: 5px 100px 5px 100px;
  border-radius: 999px;
  color: white;
  text-align: center;
  margin-top: 20px;
}

input {
  border-radius: 10px;
  background: rgb(86, 87, 115);
}
 """,
        "js": "Empty "
    },

    "32.1": {
        "html": """ <p>double calculator</p> """,
        "css": """Empty""",
        "js": """let hi = prompt();
let hello = 2;
document.write(hi * hello);
 """
    },

    "32.2": {
        "html": """<p>square calculator</p>
   """,
        "css": """Empty""",
        "js": """let square = prompt();
document.write(square * square);
 """
    },

    "34.1": {
        "html": """Empty  """,
        "css": """Empty """,
        "js": """let hlo = `Maine aaj "web development" ki duniya mein ek our 'kadan' rakha. Maine sikha ki 'string'  lichene mai / ka leya me hota hai.`;
document.write(hlo);
   """
    },

    "34.2": {
        "html": """Empty  """,
        "css": """Empty """,
        "js": """ let dusman = prompt("apna naam likho");
let massage = `mera naam "${dusman)" hai. or mujhe 'javascript string' sikhne me maja aa rahaa hai. `;
document.write(massage);
 """
    },

    "34.3": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """let naam = prompt();
let msg = `Wese to mere bahut sare dost hai, lekin unme se ${naam) sabse achha dost hai. Aur ${naam} ke sath bitaye gaye pal mujhe hamesha yaad rehte hai. `;
document.write(msg);
  """
    },

    "34.4": {
        "html": """ <h1>Addition Calculator</h1> """,
        "css": """ Empty""",
        "js": """Code has not added! """
    },

    "35.1": {
        "html": "Empty  ",
        "css": " Empty",
        "js": """let kiskaTable = +prompt("Mere aaka, batao kiska table dekhna hai ?");
let kahaTak = +prompt("table kahan tak dekhna hai ?");

for (let x = 1; x <= kahaTak; x = x + 1) {
  let table = `<p> ${kiskaTable) x ${x} = ${kiskaTable * x}</p>`;
  document.write(table);
}
 """
    },

    "35.2": {
        "html": " Empty ",
        "css": "Empty ",
        "js": """let kiskaTable = +prompt();

for (let x = 1; x <= 10; x = x + 1) {
  let table = `<p> ${kiskaTable - 1} x ${x} = ${kiskaTable * x - x} </p>`;
  document.write(table);
}
 """
    },

    "35.3": {
        "html": "Empty  ",
        "css": " Empty",
        "js": """let kiskaTable = +prompt("kiskaTable");

let kahaTak = +prompt("kahaTak");

for (let x = 1; x <= kahaTak; x = x + 1) {
  let table = `<p>${kiskaTable) x ${x} =  ${kiskaTable * x}</p>`;
  document.write(table);
}"""
    },

    "35.4": {
        "html": "Empty  ",
        "css": "Empty ",
        "js": """let kiskiGinti = +prompt("kiski ginti receive karni hai?");

for (let x = kiskiGinti; x >= 1; x--) {
  let y = `<p> ${x) </p>`;
  document.write(y);
}"""
    },

    "35.5": {
        "html": " Empty ",
        "css": " Empty",
        "js": """let kiskaTable = +prompt("kiskatable dikhana hai");

let kahaTak = +prompt("kahaTak dikhana hai");

for (let x = kahaTak; x >= 1; x = x - 1) {
  let table = `<p> ${kiskaTable) x ${x} = ${kiskaTable * x}</p>`;
  document.write(table);
}
 """
    },

    "35.6": {
        "html": "Empty  ",
        "css": "Empty",
        "js": """let count = +prompt("odd number kaha tak dikhane hai");
for (let x = 1; x <= count * 2; x = x + 2) {
  let odd = `<p>${x)</p>`;
  document.write(odd);
}"""
    },

    "35.7": {
        "html": "Empty  ",
        "css": "Empty ",
        "js": """let count = +prompt("kitne even number dikhane hai");

for (let even = 2; even <= count * 2; even = even + 2) {
  document.write(`<p> ${even) </p>`);
}"""
    },

    "35.8": {
        "html": " Empty ",
        "css": " Empty",
        "js": """let count = +prompt("kitne odd number dikhane hai");

let total = 0;

for (let odd = 1; odd <= count * 2; odd = odd + 2) {
  total = total + odd;
}
document.write(`<p>Total: ${total)</p>`);
 """
    },

    "35.9": {
        "html": " Empty ",
        "css": "Empty ",
        "js": """let count = +prompt("kitne even number dikhane hai");

let total = 0;

for(let even = 2; even <= count * 2;even = even + 2) {
 total = total+even;
  }
document.write(`<p>Total: ${total)</p>`); """
    },

    "36.1": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """let age = +prompt("tumhe tumhari maa our gf ki kasam sahi age bataoo");

if (age >= 18 && age < 75) {
  let formula =
    "Ek chamach petrol mein aadha chamach uranium daalo aur gulabi hone tak bhuno. Uske baad.... ";
  document.write(formula);
} else if (age < 18) {
  let warning =
    "beta, missile se khelne ki umr mein nuclear bomb ke sapne dekh rahe ho! ";
  document.write(warning);
} else if (age >= 75) {
  let warnningold =
    "Miya ek paavon kabr mein hai, bomb banane ko rehne hi do! ";
  document.write(warnningold);
}
  """
    },

    "36.2": {
        "html": """ Empty """,
        "css": """Empty""",
        "js": """let age = +prompt("tumhe tumhari maa kasam ssahi age batana");

if (age >= 18 && age < 65) {
  let dekh = "aap movie dekh sakte hai";
  document.write(dekh);
} else if (age < 18) {
  let nahi = "aap movie nahi dekh sakte";
  document.write(nahi);
} else if (age > 65) {
  let nahi = "aap movie nahi dekh sakte";
  document.write(nahi);
}
  """
    },

    "36.3": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """let percentage = prompt("class 12th ki parcentege");

if(percentage >= 40 && percentage < 60) {
document.write("Grade C")
  }else if(percentage >= 80) {
document.write("Grade A")
  }else if(percentage >= 60 && percentage < 80) {
document.write("Grade B")
  }else if(percentage < 40) {
document.write("Grade D")
  }     """
    },

    "37.1": {
        "html": """Empty  """,
        "css": """ Empty""",
        "js": """let naam = prompt("aap kiske Saath aaye hai");

if(naam === "papa" || naam === "mummy") {
document.write("aap result card le ja sakte hai")
  }else {
document.write("aap papa  yaa mummy ke saath aaye jabhi result card milega")
  }   """
    },

    "37.2": {
        "html": """Empty  """,
        "css": """Empty """,
        "js": """ 
let favorite = 9;

let gess = +prompt("Guess karo mera favourite number kya hai");

if(favorite === gess) {
document.write("You won. Aapko milte hain 5 aalu.! ");
  }else{
document.write("You lost. Aapko 5 hazar rupay kaa fine bharne hoga")
  }
    """
    },

    "37.3": {
        "html": """Empty  """,
        "css": """Empty """,
        "js": """ let favorite = "orange"

let gess = prompt(" guss karo konesa favourite fruit hai")

if(favorite === gess){
document.write("you won: yelo apna orange ghar le")
  }else {
document.write("you lost: aapko 150rs bharne honge")
  }"""
    },

    "37.4": {
        "html": """Empty """,
        "css": """Empty """,
        "js": """ let password = prompt("enter password");

let  chinki ="chinki";

if(password === chinki) {
}else{
document.write("Wrong password. aapko 2 saal  jail hogi")
  }
 """
    },

    "38.1": {
        "html": """  Empty""",
        "css": """Empty """,
        "js": """ function printTable(kiska,kistak){
for(let x = 1; x<= kistak; x=x+1){
let table =`<p>${kiska) x ${x} = ${kiska * x} </p>`
 document.write(table)
}
  }

let kiskaTable = +prompt("kiska table dikhana hai");
let kahaTak = +prompt("kahatak dikhana hai")

printTable(kiskaTable, kahaTak);

let kiskaTable2 = +prompt("dusra kiska table dikhana hai")
let kahaTak2 = +prompt("dusra table kahatak dikhana hai")

printTable(kiskaTable2, kahaTak2) 
   """
    },

    "38.2": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """ function printTable(kiska){
for(let x = 1; x <= 10; x = x+1){
  let table= `<p>${kiska) x ${x} = ${kiska * x}</p>`
  document.write(table)
  }
  }

let kiskaTable =+prompt("kiska table dikhana hai")
printTable(kiskaTable)

let kiskaTable2 =+prompt("dusra kiska table dikhana hai")
printTable(kiskaTable2)

let kiskaTable3 =+prompt("thisra kiska table dikhana hai")
printTable(kiskaTable3)
 """
    },

    "38.3": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """function double(investment) {
if (investment < 100000){
return 0;
  }
  let kamai = investment * 2 + 10000;
  return kamai;
  }

let aapkapaisa = +prompt("aap kitna invest karoge")
let dostkapaisa = +prompt("dost kitna invest karega")

let aapkikamai = double(aapkapaisa)
let dostkikamai = double(dostkapaisa)

document.write(`aapko milenge: Rs${aapkikamai). dost ko milenga: Rs ${dostkikamai}`);
"""
    },

    "39.1": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """while (true) {
  let x = prompt("kiska square batana hai");
  if (x === null) {
    break;
  }
  let square = x * x;
  document.write(`<p>$(square) </p>`);
} """
    },

    "40.1": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """l){
    break;
    }
  number.push(+x);
  }

number.sort((a, b)=> a-b);

let total = number.length;

for(let m = 0; m < total; m++){
let y =number[m];
let square = y * y;
document.write(`<p> $(square) </p>`)
  }
  """
    },

    "40.2": {
        "html": """ Empty """,
        "css": """ Empty """,
        "js": """let number = [];

while (true) {
  let x = prompt("kiska square dikhana hai");

  if (x === null) {
    break;
  }
  number.push(+x);
}

number.sort((a, b) => b - a);

let total = number.length;

for (let m = 0; m < total; m++) {
  let y = number[m];
  let square = y * y;
  document.write(`<p> $(square) </p>`);
}
  """
    },

    "41.1": {
        "html": """ Empty """,
        "css": """Empty """,
        "js": """let capitals = {
  'andhra Pradesh': 'Amaravati',
  'uttar pradesh': 'Lucknow',
  'madhya pradesh': 'Bhopal',
  'arunachal pradesh': 'Itanagar',
  'himachal pradesh': 'Shimla',
  'tamil Nadu': 'Chenaai',
  goa: 'Panji',
  maharashtra: 'Mumbai',
  uttrakhand: 'Dehradun',
  assam: 'Dispur',
  bihar: 'Patna',
  haryana: 'Chandigarh',
  jharkhand: 'Ranchi',
  chattisgarh: 'Raipur',
  gujarat: 'Gandhi nagar',
  karnataka: 'Banglore',
  manipur: 'Imphal',
  Kerala: 'Tiruvannantpuram',
  Meghalaya: 'Shillong',
  Mizoram: 'Aizawl',
  Nagaland: 'Kohima',
  Odisha: 'Bhubaneshwar',
  Punjab: 'Chandigarh',
  Rajasthan: 'jaipur',
  Sikkim: 'Gangtok',
  Telangana: 'Hydrabad',
  Tripura: 'Agartla',
  'West Bengal': 'Kolkata' 
};
  let state = prompt('Kiski Rajdhani pata karni hai?');
  let data = capitals[state];
document.write(data);
    """
    },

    "42.1": {
        "html": """Empty  """,
        "css": """Empty """,
        "js": """ let number = [];

while(true) {
let x = prompt("kiska square dikhana hai");

  if(x === null){
  break;
  }
  number.push(+x)
  }

number.sort((a,b) => b-a);

let total = number.length;

for(let m = 0; m < total; m++){
let y = number[m]
let square = y * y;
document.write(<p>$(square)  </p>);
  } """
    },

    "45.1": {
        "html": """ <p id="output"></p>
<input type="number" placeholder="Enter Number one" id="input1" />
<input type="number" placeholder="Enter Number two" id="input2" />
<button onclick="showAdd()">Add</button>
<button onclick="showSubtract()">Subtract</button>
<button onclick="showMultiply()">Multiply</button>
<button onclick="showDivide()">Divide</button>
  """,
        "css": """Empty """,
        "js": """ function showAdd() {
  let myInput = document.getElementById("input1");
  let myInput1 = document.getElementById("input2");

  let a = +myInput.value;
  let b = +myInput1.value;

  myInput.value = " ";
  myInput1.value = " ";

  let add = a + b;

  let resultTag = document.getElementById("output");

  resultTag.innerHTML = add;
}

function showSubtract() {
  let myInput = document.getElementById("input1");
  let myInput1 = document.getElementById("input2");

  let a = +myInput.value;
  let b = +myInput1.value;

  myInput.value = "";
  myInput1.value = "";

  let subtract = a - b;

  let resultTag = document.getElementById("output");

  resultTag.innerHTML = subtract;
}

function showMultiply() {
  let myInput = document.getElementById("input1");
  let myInput1 = document.getElementById("input2");

  let a = +myInput.value;
  let b = +myInput1.value;

  myInput.value = "";
  myInput1.value = "";

  let multiply = a * b;

  let resultTag = document.getElementById("output");

  resultTag.innerHTML = multiply;
}

function showDivide() {
  let myInput = document.getElementById("input1");
  let myInput1 = document.getElementById("input2");

  let a = +myInput.value;
  let b = +myInput1.value;

  myInput.value = "";
  myInput1.value = "";

  let divide = a / b;

  let resultTag = document.getElementById("output");

  resultTag.innerHTML = divide;
}
 """
    },

    "46.1": {
        "html": """ <h1 id="jadu">Namaste Duniya!</h1>
<button onclick="setColor('red')">red</button>
<button onclick="setColor('green')">green</button>
<button onclick="setColor('blue')">blue</button>
<button onclick="hide()">gayab</button>
<button onclick="show()">show</button>  """,
        "css": """Empty """,
        "js": """function setColor(color) {
  let heading = document.getElementById('jadu');
  
heading.style.color = color; 
  
  }
function hide() {
 let heading = document.getElementById('jadu');
  
 heading.style.visibility = 'hidden';
  
  }
function show() {
let heading = document.getElementById('jadu');
  
heading.style.visibility = 'visible';
}  """
    },

    "47.1": {
        "html": """ <button>Login</button>  """,
        "css": """button{
  font-size: 20px;
  color: white;
  background: skyblue;
  border: 1px solid skyblue;
  border-radius: 5px;
  padding: 2px 10px;
  }

:hover{
   color: skyblue;
   background: white;
}  """,
        "js": """ Empty"""
    },

    "47.2": {
        "html": """<div class="container">
  <input type="text" placeholder="Your Username">
  <input type="password" placeholder="Your Password">
  <button> Login</button>
</div>    """,
        "css": """input{
  background: yellow;
}
input:hover{
  background: lightgreen;
}
input:focus{
  background: lightpink;
}
button{
  color: white;
  background: lightblue;
  padding: 6px 12px;
  border: 2px solid lightblue;
  border-radius: 8px;
}
button:hover{
  color: lightblue;
  background: white;
} """,
        "js": """ Empty """
    },

    "48.1": {
        "html": """<h1 id="xyz">Namaste Duniya!</h1>
<button  onclick="setColor('red',event)">red</button>
<button onclick="setColor('green',event)">green</button>
<button onclick="setColor('blue',event)">blue</button>
<button onclick="hide()">gayab</button>
<button onclick="show()">show</button>
<p>Color <span id="counter">0</span>baar change hua. </p>   """,
        "css": """button{
  background-color: skyblue;
}
button:disabled{
  background-color: lightgray;
  cursor: not-allowed;
}  """,
        "js": """function setColor(color, event) {
  
  let heading = document.getElementById("xyz");

  heading.style.color = color;

  let span = document.getElementById("counter");
  let count = +span.innerHTML;

  span.innerHTML = count + 1;

  const allButtons =                                  document.getElementsByTagName("button");

  for (let i = 0; i < allButtons.lenght; i++) {
    const b = allButtons[i];
    b.disabled = false;
  }
  
  const button = event.target;
  button.disabled = true;
}

function hide() {
  let heading = document.getElementById("xyz");

  heading.style.visibility = 'hidden';
}

function show() {
  let heading = document.getElementById("xyz");

  heading.style.visibility = 'visible';
}  """
    },

    "49.1": {
        "html": """<h1>Simple E-Commerce Website</h1>
 <input type="text" id="searchInput" placeholder="Product ka name search kre" onkeyup="searchProduct()">
 <div id="products" class="products"></div>
 <div id="message" class="not-found"></div>   """,
        "css": """body{
  font-family: Arial, sans-serif;
  margin: 20px;
  background-color: #f0f0f0;
}

input{
  padding: 10px;
  font-size: 16px;
  width: 300px;
}

.products{
margin-top: 20px;
}

.product-item{
  background-color: white;
  padding: 15px;
  margin: 10px;
  border: 1px solid #ccc;
  display: inine-block;
  width: 200px;
  text-align: center;
}

.not-found{
  color: red;
  font-size: 20px;
}
   """,
        "js": """ const products = [
  'iPhone',
  'smartwatch',
  'bottle',
  'boll pen',
  'gel pen',
  'pencil',
  'lamp',
  'mouse',
  'keyboard',
  'monitor',
  'printer'
];

function searchProduct() {
  let input = document.getElementById('searchInput').value.toLowerCase();
  let filteredProducts = products.filter(product => product.toLowerCase().includes(input));

  let productsDiv = document.getElementById('products');
  let messageDiv = document.getElementById('message');
  
  productsDiv.innerHTML = '';
  messageDiv.innerHTML = '';

if (input === "") {
  displayProducts(products);
} else if (filteredProducts.length > 0) {
  displayProducts(filteredProducts);
} else {messageDiv.innerHTML = 'koi product nahi mila';}
}

function displayProducts(productList) {
  let productsDiv = document.getElementById('products');

  productList.forEach(product => { let productItem = `<div class="product-item">${product}</div>`;
  productsDiv.innerHTML += productItem;});
}


   window.onload = () => displayProducts(products);



  """
    },

    "50.1": {
        "html": """ <p id="numbers">3, 23, 7, 17, 42, 9, 22, 4, 33, 88, 13, 27, 10, 64</p>

<button onclick="showOdd()"> Odd </button>
<button onclick="showEven()"> Even </button>
<p id="numberList"></p>    """,
        "css": """#numbers {
  background: gray;
  padding: 10px;
  border-radius: 10px;
  color: white;
  width: max-content;
}

button {
  padding: 5px 20px 5px 20px;
}
    """,
        "js": """let numbers = [3, 23, 7, 17, 42, 9, 22, 4, 33, 88, 13, 27, 10, 64];

function showOdd() {
let oddNumbers = numbers.filter(num => num % 2 !== 
0);

document.getElementById('numberList').innerHTML = 
oddNumbers.join(' ,'); 
       }

function showEven() {
let evenNumbers = numbers.filter(num => num % 2 === 
0);

document.getElementById('numberList').innerHTML = 
evenNumbers.join(' ,');
        }
    """
    },

    "47.2": {
        "html": """  """,
        "css": """ """,
        "js": """ """
    },

}
