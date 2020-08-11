const http = require('http')        // brought lib 'http'
const fs = require('fs')            // brought lib 'fs'
const port = 3000

const server = http.createServer(function(req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' })
    fs.readFile('README.html', function(error, data) {
        if (error) {
            res.writeHead(404)
            res.write('Error: File Not Found')
        }
        else
            res.write(data)
        res.end()
    })
})

server.listen(port, function(error) {
    if (error)
        console.log('err:', error)
    else
        console.log("server's online: http://localhost:3000/")
})
