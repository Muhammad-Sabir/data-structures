const string = 'aabcddklmn';

function longestSubstring(str) {
	let subElements = {};
	let max = 1;

	for (let i = 0; i < str.length; i++) {
		if (str[i] == str[i + 1]) {
			subElements = {};
			continue;
		}

		let char = str[i];

		if (subElements[char] == 1) subElements = {};

		subElements[char] = 1;

		let length = Object.keys(subElements).length;
		if (length > max) max = length;
	}

	return max;
}

console.log(longestSubstring(string));
