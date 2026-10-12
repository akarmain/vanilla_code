var twoSum = function (nums, target) {
	let map = {}
	for (let i = 0; i < nums.length; i++) {
		let x = target - nums[i]
		if (map[x] !== undefined) return [map[x], i]
		map[nums[i]] = i
	}
}
if (require.main === module) {
	// nums = [2, 3, 3]
	// target = 6
	// console.log(twoSum([2, 3, 3], 6))
	console.log(1 == 1)
	console.log(1 == '1')
	console.log(1 == '5')
	console.log(1 == "5")
	console.log(1.0 == "1.0")
	console.log(1.00000 == "1.0")
	console.log(1.00000 == "1")
}
