let todo=document.querySelector('.todo')
let plusBtn=document.querySelector('#plus')
let minusBtn=document.querySelector('#minus')
let single=`
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="Kategoriya..">
                        <div class="input-group-append">
                            <span class="input-group-text" id="plus" onclick='addBlock()'>+</span>
                            <span class="input-group-text" id="minus" onclick='removeBlock(this)'>-</span>
                        </div>
                    </div>

`

let content=single;


function addBlock(){
    content+=single
    console.log('click isleyir fikret')
    todo.innerHTML=content;
}

function removeBlock(elem){
   todo.removeChild( elem.parentElement.parentElement)
}

