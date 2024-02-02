// 快速排序 QuickSort in JavaScript
/**
 * @param {number[]} array 
 * @param {number} begin 
 * @param {number} end 
 */
function quickSort(array, begin, end) {
  if (end <= begin) {
    return
  }
  let pivot = partition(array, begin, end)
  quickSort(array, begin, pivot - 1)
  quickSort(array, pivot + 1, end)
}
/**
 * @param {number[]} array 
 * @param {number} begin 
 * @param {number} end 
 */
function partition(array, begin, end) {
  console.log('array ->', array, begin, end)
  let pivot = end
  let counter = begin

  for (let i = begin; i < end; i++) {
    if (array[i] < array[pivot]) {
      console.log('< ->', array[counter], array[i])
      // 交换 i 和 counter 的位置
      let temp = array[counter]
      array[counter] = array[i]
      array[i] = temp
      counter++
    }
  }
  console.log('array1 ->', array)
  // 交换 counter 和 pivot 的位置
  let temp = array[pivot]
  array[pivot] = array[counter]
  array[counter] = temp
  console.log('array2 ->', array)

  return counter
}

let array = [3, 2, 5]
quickSort(array, 0, array.length - 1)
console.log('array ->', array)
// let pivot = partition(array, 0, 2)
// console.log('pivot ->', pivot)