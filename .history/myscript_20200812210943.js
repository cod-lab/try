// const btnGetLatestRepos = document.getElementById('btnGetLatestRepos');
// btnGetLatestRepos.addEventListener('mouseover', get5Repos);

window.addEventListener('load',get5Repos);

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
            a.textContent.fontcolor('orange') = result[i].full_name.replace('cod-lab/','');
            // a.textContent.fontcolor('orange');

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
