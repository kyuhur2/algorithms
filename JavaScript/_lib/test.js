export function assert( outcome, test_number ) { 
    var passFail = outcome ? 'Pass' : 'Fail';
    console.log(`Test ${test_number} : `, passFail);
    return outcome;
};

export function isEqual(a, b) {
    return a.join() === b.join();
}