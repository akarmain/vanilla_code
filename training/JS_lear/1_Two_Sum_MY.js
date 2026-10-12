function main() {
	console.log('Hello, JS 1 !')
}

function main() {
	console.log('Hello, JS 2 !')
}

var twoSum = function (nums, target) {
	const ans = []
	for (let i = 0; i < nums.length; i++) {
		for (let j = 0; j < nums.length; j++) {
			if (nums[i] + nums[j] == target & i != j) {
				ans.push(i)
				ans.push(j)
				return ans
			}
		}
	}
}
if (require.main === module) {
	let nums = [2, 3, 3]
	let target = 6
	let ans = twoSum(nums, target)
	console.log(ans)
}
