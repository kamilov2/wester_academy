const offSet = 100;

const scrollUp = document.querySelector(".scroll-up")
const getTop = () => window.pageYOffset || document.documentElement.scrollTop;
window.addEventListener('scroll', () => {
    if (getTop() > offSet) {
        scrollUp.classList.add("active")
    } else {
        scrollUp.classList.remove("active")
    }
})
// voice start
const voiceImg = document.querySelector(".voice__img")
const voiceGif = document.querySelector(".voice__video")
const audio = document.getElementById("myAudio");
const voice = document.querySelector(".voice")


voice.addEventListener("click", () => {
    if (audio.paused) {
        audio.play();
        voiceImg.classList.remove("actVoice")
        voiceGif.classList.add("actVoice")
    } else {
        audio.pause();
        voiceImg.classList.add("actVoice")
        voiceGif.classList.remove("actVoice")
    }
})
// voice end

scrollUp.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
})



document.addEventListener('shown.bs.collapse', function (event) {
    var activeHeader = event.target.parentElement.querySelector('.butt');
    if (activeHeader) {
        activeHeader.classList.add('myActivee');
    }
});

document.addEventListener('hidden.bs.collapse', function (event) {
    var activeHeader = event.target.parentElement.querySelector('.butt');
    if (activeHeader) {
        activeHeader.classList.remove('myActivee');
    }
});

// slider start
let position = 0;
const slidesToShow = 4;
const slidesToScroll = 2;
const container = document.querySelector(".slider-container");
const track = document.querySelector(".slider-container__list");
const items = document.querySelectorAll(".slider-container__list__slider");
const btnPrev = document.getElementById("prev");
const btnNext = document.getElementById("next");

const itemsCount = items.length;
const itemWidth = 390 //container.clientWidth / slidesToShow;
const movePosition = container.clientWidth === 400 ? 320 : container.clientWidth === 767 ? 600 : slidesToScroll * itemWidth;


btnNext.addEventListener("click", () => {
    const itemsLeft = itemsCount - (Math.abs(position) + slidesToShow * itemWidth) / itemWidth;

    position -= itemsLeft >= slidesToScroll ? movePosition : itemsLeft * itemWidth;

    setPosition();
    checkBtns();
});

btnPrev.addEventListener("click", () => {
    const itemsLeft = Math.abs(position) / itemWidth;

    position += itemsLeft >= slidesToScroll ? movePosition : itemsLeft * itemWidth;

    setPosition();
    checkBtns();
});

const setPosition = () => {
    track.style.transform = `translateX(${position}px)`;
};

const checkBtns = () => {
    btnPrev.disabled = position === 0;
    btnNext.disabled = position <= -(itemsCount - slidesToShow) * itemWidth;
};


checkBtns();
// slider end


function openModal() {
    document.getElementById('pop-up').style.display = 'flex';
    document.getElementById('pop-up-close').style.display = 'block';
}

function closeModal() {
    document.getElementById('pop-up').style.display = 'none';
    document.getElementById('pop-up-close').style.display = 'none';
    document.body.style.overflow = 'visible'; // or 'auto'
}

const popUp = () => {
    openModal()
    document.body.style.overflow = 'hidden';
}

const time = 30000

setTimeout(popUp, time);








//
document.addEventListener('DOMContentLoaded', function () {
    const handleContextMenu = function (e) {
        e.preventDefault();
    };

    const handleKeyDown = function (e) {
        if (e.keyCode === 123) {
            e.preventDefault();
        } else if (e.ctrlKey && e.shiftKey && e.keyCode === 'I'.charCodeAt(0)) {
            e.preventDefault();
        } else if (e.ctrlKey && e.shiftKey && e.keyCode === 'C'.charCodeAt(0)) {
            e.preventDefault();
        } else if (e.ctrlKey && e.shiftKey && e.keyCode === 'J'.charCodeAt(0)) {
            e.preventDefault();
        } else if (e.ctrlKey && e.keyCode === 'U'.charCodeAt(0)) {
            e.preventDefault();
        }
    };

    document.addEventListener('contextmenu', handleContextMenu);
    document.addEventListener('keydown', handleKeyDown);

    window.addEventListener('beforeunload', function () {
        document.removeEventListener('contextmenu', handleContextMenu);
        document.removeEventListener('keydown', handleKeyDown);
    });
});
//
