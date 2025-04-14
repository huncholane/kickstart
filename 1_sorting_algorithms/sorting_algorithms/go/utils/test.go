package utils

type Test struct {
	f func([]int)
	numTests int
	size int
	left int
	right int
}

// DefaultTest initializes a Test with:
//   - 10 tests
//   - Range: -100 to 100
//   - Size: 100
func DefaultTest(f func([]int)) *Test {
	return &Test{numTests:10,size:100,left:-100,right:100}
}

// Run tests using the test config
func (t *Test) Run() int {
	passed:=0
	for range t.numTests {
		arr:=CreateArr(t.size,t.left,t.right)
		t.f(arr)
		if DidSort(arr) {
			passed+=1
		}
	}
	return passed
}