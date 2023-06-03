
import http from 'k6/http';
import { sleep, check } from 'k6';
export const options = {
    vus: 10,
    duration: '15s',
};

var port = __ENV.K6_CALLEE_PORT
var endpoint = __ENV.K6_CALLEE_ENDPOINT

console.log(port)
console.log(endpoint)
console.log("hitting: " + endpoint)

export default function () {
    const params = { 'headers': { 'traceparent': '27b1c61822bcdb4736513466dde98b92' } }
    // console.log("made req, waiting...")
    const res = http.get('http://127.0.0.1:' + port + "/" + endpoint, params);
    // console.log("done")
    check(res, { 'status was 200': (r) => r.status == 200 });
    // console.log("checked")
    sleep(15 / 1000);
}