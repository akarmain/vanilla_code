function Hi() {
	return 'Hello, World!'
}

if (require.main === module) {
	console.log(Hi())
	// const add = function (a, b) {
	// 	return a + b
	// }
	// console.log(add(1,2))
	const add = (a) => a**a;
	console.log(add(4))
	const getUser = (name, age) => ({ name: name, age: age });
	
	console.log(getUser("a", 5))

}
