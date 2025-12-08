function findMax(arr) {
    let max = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

const numbers = [12, 45, 7, 89, 23];
console.log("Array:", numbers);
console.log("Maximum element:", findMax(numbers));
