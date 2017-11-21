package simplemath

import "testing"

func TestSqrt1(t *testing.T) {
	v := Sqrt(16)
    t.Errorf("test Errorf")

	if v != 3 {
		t.Errorf("Sqrt(16) filed. Got %v, expected 4.", v)
	}


}
