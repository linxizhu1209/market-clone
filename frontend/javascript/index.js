const calcTime = (timestamp) => {
  const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
  // 세계시간기준으로 timestamp가 나오기때문에 -9시간을 해줘야지 한국시간이됨
  const flowTime = new Date(curTime - timestamp);
  const hour = flowTime.getHours();
  const min = flowTime.getMinutes();
  const sec = flowTime.getSeconds();

  if (hour > 0) return `${hour}시간 전`;
  else if (min > 0) return `${min}분 전`;
  else if (sec > 0) return `${sec}초 전`;
  else return "방금 전";
};

const renderData = (data) => {
  const main = document.querySelector("main");

  //   data.reverse() // 데이터 배열을 뒤집는 역할
  data.reverse().forEach(async (obj) => {
    const Div = document.createElement("div");
    Div.className = "items-list";

    const imgDiv = document.createElement("div");
    imgDiv.className = "items-list__img";

    const img = document.createElement("img");
    const res = await fetch(`/images/${obj.id}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    img.src = url;

    const InfoDiv = document.createElement("div");
    InfoDiv.className = "items-list__info";

    const InfoTitleDiv = document.createElement("div");
    InfoTitleDiv.className = "items-list__info-title";
    InfoTitleDiv.innerText = obj.title;

    const InfoMetaDiv = document.createElement("div");
    InfoMetaDiv.className = "items-list__info-meta";
    InfoMetaDiv.innerText = obj.place + " " + calcTime(obj.insertAt);

    const InfoPriceDiv = document.createElement("div");
    InfoPriceDiv.className = "items-list__info-price";
    InfoPriceDiv.innerText = obj.price;

    InfoDiv.appendChild(InfoTitleDiv);
    InfoDiv.appendChild(InfoMetaDiv);
    InfoDiv.appendChild(InfoPriceDiv);
    imgDiv.appendChild(img);
    Div.appendChild(imgDiv);
    Div.appendChild(InfoDiv);
    main.appendChild(Div);
  });
};

const fetchList = async () => {
  const accessToken = localStorage.getItem("token");
  const res = await fetch("/items", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  if (res.status === 401) {
    alert("로그인이 필요합니다!!");
    window.location.pathname = "/login.html";
    return;
  }
  const data = await res.json();
  renderData(data);
};

fetchList();
