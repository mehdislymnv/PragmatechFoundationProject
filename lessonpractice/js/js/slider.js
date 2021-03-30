let containerWidth=document.querySelector('.container').clientWidth;

let sliderContent=document.querySelector('.slider-content');
let slides=document.querySelectorAll('.slide');
let leftBtn=document.querySelector('.leftBtn')
let rightBtn=document.querySelector('.rightBtn')
pos=0;
for(i=0;i<slides.length;i++){
    slides[i].style.width=containerWidth+'px';
}

sliderContent.style.width=containerWidth*slides.length+'px';

leftBtn.addEventListener('click',function(){
    sliderContent.style.transform=`translateX(${pos}px)`
    pos+=containerWidth;
})
rightBtn.addEventListener('click',function(){
    sliderContent.style.transform=`translateX(${pos}px)`
    pos-=containerWidth;
})