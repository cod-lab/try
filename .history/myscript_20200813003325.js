// const btnGetLatestRepos = document.getElementById('btnGetLatestRepos');
// btnGetLatestRepos.addEventListener('mouseover', get5Repos);

window.addEventListener('load',get5Repos);

const btnDisplay  = document.querySelector('btnDisplay');
const btnDownload  = document.querySelector('btnDownload');
const imgConverted  = document.querySelector('imgConverted');
const myCanvas  = document.querySelector('myCanvas');

const ctx = myCanvas.getContext('2d');

ctx.font = "50px Roboto";
ctx.fillstyle = "red";
ctx.filltext('decode', 100,100);
ctx.fillReact(200,150,150,75);

btnDisplay.addEventListener('click',function()) {
    const dataURI = myCanvas.toDataURL();
    
}

const divResult = document.getElementById('divResult');

async function get5Repos() {
    // clear();
    
    const url = "https://api.github.com/users/cod-lab/repos?sort=created";     // get my repos in desc order they created
    const response = await fetch(url);
    const result = await response.json();

    // console.log(result)
    // result.forEach(i=> {

    var j=-1;
    for(var i in result) {
        if(result[i].fork == false)
        {
            var li = document.createElement('li');
            var a = li.appendChild(document.createElement('a'));

            // const anchor = document.createElement('a')
            a.href = result[i].html_url;
            a.textContent = result[i].full_name.replace('cod-lab/','');
            // a.textContent.fontcolor('red');

            // anchor.classList.add("cls1")

            // divResult.appendChild(anchor)
            // divResult.appendChild(document.createElement('br'))
            divResult.appendChild(li);

            ++j;
        }
        if(j==4) break;
    }
}

// async function clear() {              // clear earlier result before printing new
//     while(divResult.firstChild)
//         divResult.removeChild(divResult.firstChild);
// }

console.log('this is js file');
