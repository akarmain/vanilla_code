var fib_algos = function (n) {
	let arr = [1, 1]
	for (let i = 1; i < n - 1; i++) {
		arr.push(arr[i] + arr[i - 1])
	}
	return arr.pop()
}

var fib_rec_bed = function (n) {
	if (n <= 2) {
		return 1
	} else {
		return fib_rec_bed(n - 1) + fib_rec_bed(n - 2)
	}
}

var fib_rec_cash = function (n) {
	for (let i = 0; i < n; i++) {
		console.log(i)
	}
}

function fib_memoize(n) {
	const cache = {0: 0, 1:1}
	i = 2
	while (!(n in cache)){
		cache[i] = cache[i-1] + cache[i-2]
		i++
	}
	return cache[n]
}

if (require.main === module) {
	console.log(fib_memoize(10))
}
