console.log("world")

// let mountDir = "/mnt";
// pyodide.FS.mkdir(mountDir);
// pyodide.FS.mount(pyodide.FS.filesystems.IDBFS, { root: "." }, mountDir);
// pyodide.FS.syncfs(false, callback_func);
// document.getElementById("inandop").innerHTML = "./somenew.xlsx";



let namefile=document.getElementById("inandop").value;

console.log(namefile);
document.getElementById('newdownload').setAttribute('href',namefile);

// document.getElementById('newdownload').href(namefile);

function downloadfile(){
  const some = document.createElement("a");
  some.download = newfile;
  document.body.appendChild(some);
  some.click()
  document.body.removeChild(some);
}