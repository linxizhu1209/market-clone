<script>
  let hour = new Date().getHours()
  let min = new Date().getMinutes()

</script>
    <header>
      <div class="info-bar">
        <div class="info-bar__time">{hour}:{min}</div>
        <div class="info-bar__icons">
          <img src="./assets/chart-bar.svg" alt="chart-bar" />
          <img src="./assets/wifi.svg" alt="wifi" />
          <img src="./assets/battery.svg" alt="battery" />
        </div>
      </div>
      <div class="menu-bar">
        <div class="menu-bar__location">
          <div>수곡동</div>
          <div class="menu-bar__location-icons">
            <img src="./assets/arrow.svg" alt="arrow" />
          </div>
        </div>
        <div class="menu-bar__icons">
          <img src="./assets/search.svg" alt="search" />
          <img src="./assets/menu.svg" alt="menu" />
          <img src="./assets/alert.svg" alt="alert" />
        </div>
      </div>
    </header>
    <main>
        <div id="messageWin" style="display: none;">
        <ul id="message-ul">
        </ul>
      </div>
        <input type="text" id="message-input" style="display: none;" placeholder="메시지를 입력해주세요" />
        <a href="#/write" class="write-btn">+글쓰기</a>
    </main>
    <footer>
      <div class="footer-block">
        <div class="footer-icons">   
            <div class="footer-icons__img"><img src="./assets/home.svg" alt="home" /></div>
            <div class="footer-icons__des">홈</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img"><img src="./assets/doc.svg" alt="document" /></div>
          <div class="footer-icons__des">동네생활</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img"><img src="./assets/location.svg" alt="location" /></div>
          <div class="footer-icons__des">내 근처</div>
        </div>
        <div class="footer-icons" id="messenger">
          <div class="footer-icons__img"><img src="./assets/message.svg" alt="message" /></div>
          <div class="footer-icons__des">채팅</div>
        </div>
        <div class="footer-icons">
            <div class="footer-icons__img"><img src="./assets/user.svg" alt="user" /></div>
        <div class="footer-icons__des">나의 당근</div>
    </div>
    </footer>   
     <div class="media-info-msg">화면 사이즈를 줄여주세요.</div>

     <style>
      .info-bar__time{
        color:blue
      }
     </style>