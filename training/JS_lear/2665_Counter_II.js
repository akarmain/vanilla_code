/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
	const save = init
	let data = save
	function increment() {
		return ++data
	}
	function decrement() {
		return --data
	}
	function reset() {
		data = init
		return init
	}
	return {
		increment,
		reset,
		decrement
	}
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
if (require.main === module) {
	const counter = createCounter(5)
	console.log(counter.increment()) // 6
	console.log(counter.reset()) // 5
	console.log(counter.decrement()) // 4
}
