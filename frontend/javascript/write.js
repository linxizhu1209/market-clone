const handleSubmitForm = async () => {
  event.preventDefault();
  const body = new FormData(form);
  body.append("insertAt", new Date().getTime());

  try {
    const res = await fetch("/items", {
      method: "POST",
      body,
    });
    const data = await res.json();
    if (data === "200") window.location.pathname = "/";
  } catch (e) {
    console.error("이미지 업로드에 실패하였습니다.");
  }
};

const form = document.getElementById("write-form");
form.addEventListener("submit", handleSubmitForm);
