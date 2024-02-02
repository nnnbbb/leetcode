
/**
 * @param {number[]} array 
 */
function mergeSort(array) {
  if (array.length <= 1) {
    return
  }
  let mid = Math.floor(array.length / 2)
  let left = array.slice(0, mid)
  let right = array.slice(mid)
  
  mergeSort(left)
  mergeSort(right)

  let i = j = k = 0

  while (i < left.length && j < right.length) {

    if (left[i] < right[j]) {
      array[k] = left[i]
      i++
    } else {
      array[k] = right[j]
      j++
    }
    k++
  }

  while (i < left.length) {
    array[k] = left[i]
    i++
    k++
  }
  
  while (j < right.length) {
    array[k] = right[j]
    j++
    k++
  }
}
let array = [6, 5, 12, 9, 1]

mergeSort(array)
console.log('array ->', array)
