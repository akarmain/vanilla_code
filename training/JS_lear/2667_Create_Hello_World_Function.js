/**
 * @return {Function}
 */
var createHelloWorld = function () {
	return function (...args) {
		console.log('Hello World')
	}
}

if (require.main === module) {
	const f = createHelloWorld()
	f({}, null, 42) // "Hello World"
}
