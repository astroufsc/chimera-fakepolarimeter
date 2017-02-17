chimera-fakepolarimeter plugin
==============================

A fake polarimeter plugin for the chimera observatory control system
https://github.com/astroufsc/chimera.

Usage
-----

Install according to the example below and configure the four virtual polarimetric filter wheels with the example also
below.


Installation
------------

Installation instructions. Dependencies, etc...

::

    pip install -U git+https://github.com/astroufsc/chimera-fakepolarimeter.git


Configuration Example
---------------------

Here goes an example of the configuration to be added on ``chimera.config`` file.

::

    filterwheels:
      - name: pol_filter
        type: FakePolarimeterFilterWheel
        filters: "U B V R I"

      - name: pol_analyzer
        type: FakePolarimeterAnalyzerWheel
        filters: "CLEAR CALCITE VIS RED"

      - name: pol_waveplate
        type: FakePolarimeterWavePlate
        filters: "0.00 22.50 45.00 67.50 90.00 112.50 135.00 157.50 180.00 202.50 225.00 247.50 270.00 292.50 315.00 337.50"

      - name: pol_dither
        type: FakePolarimeterDither
        filters: "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17"

      - name: polarimeter
        type: FakePolarimeter
        device: /FakePolarimeterFilterWheel/pol_filter,/FakePolarimeterAnalyzerWheel/pol_analyzer,/FakePolarimeterWavePlate/pol_waveplate,/FakePolarimeterDither/pol_dither

Testing
-------

To test the example configuration:

::

    ## Check initial positions
    chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter --info
    chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer --info
    chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate --info
    chimera-filter --wheel /FakePolarimeterDither/pol_dither --info
    ## Move
    chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter -f R
    chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer -f VIS
    chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate -f 22.50
    chimera-filter --wheel /FakePolarimeterDither/pol_dither -f 4
    ## Check initial positions again
    chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter --info
    chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer --info
    chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate --info
    chimera-filter --wheel /FakePolarimeterDither/pol_dither --info

Sample output of the test:

::

    $ chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter --info
    ======================================== 
    Filter Wheel: /FakePolarimeterFilterWheel/pol_filter (None) 
    Current Filter: R 
    Available filters: U B V R I 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer --info
    ======================================== 
    Filter Wheel: /FakePolarimeterAnalyzerWheel/pol_analyzer (None) 
    Current Filter: VIS 
    Available filters: CLEAR CALCITE VIS RED 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate --info
    ======================================== 
    Filter Wheel: /FakePolarimeterWavePlate/pol_waveplate (None) 
    Current Filter: 22.50 
    Available filters: 0.00 22.50 45.00 67.50 90.00 112.50 135.00 157.50 180.00 202.50 225.00 247.50 270.00 292.50 315.00 337.50 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterDither/pol_dither --info
    ======================================== 
    Filter Wheel: /FakePolarimeterDither/pol_dither (None) 
    Current Filter: 4 
    Available filters: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 
    ======================================== 


    $ chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter -f R
    Changing current filter to R ... OK 
    $ chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer -f VIS
    Changing current filter to VIS ... OK 
    $ chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate -f 22.50
    Changing current filter to 22.50 ... OK 
    $ chimera-filter --wheel /FakePolarimeterDither/pol_dither -f 4
    Changing current filter to 4 ... OK 



    $ chimera-filter --wheel /FakePolarimeterFilterWheel/pol_filter --info
    ======================================== 
    Filter Wheel: /FakePolarimeterFilterWheel/pol_filter (None) 
    Current Filter: R 
    Available filters: U B V R I 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterAnalyzerWheel/pol_analyzer --info
    ======================================== 
    Filter Wheel: /FakePolarimeterAnalyzerWheel/pol_analyzer (None) 
    Current Filter: VIS 
    Available filters: CLEAR CALCITE VIS RED 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterWavePlate/pol_waveplate --info
    ======================================== 
    Filter Wheel: /FakePolarimeterWavePlate/pol_waveplate (None) 
    Current Filter: 22.50 
    Available filters: 0.00 22.50 45.00 67.50 90.00 112.50 135.00 157.50 180.00 202.50 225.00 247.50 270.00 292.50 315.00 337.50 
    ======================================== 
    $ chimera-filter --wheel /FakePolarimeterDither/pol_dither --info
    ======================================== 
    Filter Wheel: /FakePolarimeterDither/pol_dither (None) 
    Current Filter: 4 
    Available filters: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 
    ======================================== 

    ### Changing the meta filter wheel position ###
    $ chimera-filter --wheel /FakePolarimeter/polarimeter --info
    ========================================
    Filter Wheel: /FakePolarimeter/polarimeter (/FakePolarimeterFilterWheel/pol_filter,/FakePolarimeterAnalyzerWheel/pol_analyzer,/FakePolarimeterWavePlate/pol_waveplate,/FakePolarimeterDither/pol_dither)
    Current Filter: U,CLEAR,0.00,0
    Available filters: NONE
    ========================================
    $ chimera-filter --wheel /FilterWheel/5 -f R,CALCITE,90.00,1
    Changing current filter to R,CALCITE,90.00,1 ... OK
    $ chimera-filter --wheel /FakePolarimeter/polarimeter --info
    ========================================
    Filter Wheel: /FakePolarimeter/polarimeter (/FakePolarimeterFilterWheel/pol_filter,/FakePolarimeterAnalyzerWheel/pol_analyzer,/FakePolarimeterWavePlate/pol_waveplate,/FakePolarimeterDither/pol_dither)
    Current Filter: R,CALCITE,90.00,1
    Available filters: NONE
    ========================================


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-fakepolarimeter/
