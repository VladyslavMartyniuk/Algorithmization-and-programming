================================================================================
            FULL AUTOMATIC BASKETBALL GOAL COUNTER ALGORITHM
================================================================================

SYSTEM OVERVIEW:
This algorithm combines a court tracking system (tracking shooter position) 
with an optical net sensor to automatically detect made baskets and award 
the correct number of points (1, 2, or 3).


SYSTEM VARIABLES & HARDWARE INPUTS:
* S_total         : Integer (Cumulative match score, initial value = 0)
* netSensorState  : Enum (Optical beam status: CLEAR or BROKEN)
* shooterPosition : Enum (Feet location at release: FREE_THROW, INSIDE_ARC, OUTSIDE_ARC)
* isShotInFlight  : Boolean (Set to TRUE when a shot attempt is registered)
* points          : Integer (Calculated point value for the current goal: 1, 2, or 3)
* t               : Integer (System clock tick in seconds)


=========================== MAIN ALGORITHM FLOW ===========================

                          [ START ]
                              |
                              v
                /   Is shot released?   \
               /                         \
              +---------------------------+
                |                       |
             ( YES )                  ( NO )
                |                       |
                v                       v
     [ Record shooterPosition ]    [ Continue ]
     [ Set isShotInFlight = TRUE ]      |
                |                       |
                +-----------+-----------+
                            |
                            v
                  /   Is t % 1 == 0?   \
                 /                      \
                +------------------------+
                  |                    |
               ( YES )               ( NO )
                  |                    |
                  v                    v
  / Is netSensorState == BROKEN? \   [ Wait / t + 1 ]
 /                                \    |
+----------------------------------+   |
  |                              |     |
( YES )                        ( NO )  |
  |                              |     |
  v                              v     v
/ What is shooterPosition? \   [ Keep score ]
  |            |         |       |     |
(FREE_THROW)(INSIDE)(OUTSIDE)    |     |
  |            |         |       |     |
  v            v         v       |     |
[pts = 1]  [pts = 2] [pts = 3]   |     |
  |            |         |       |     |
  +------------+---------+       |     |
               |                 |     |
               v                 |     |
  [ S_total = S_total + pts ]    |     |
  [ Update Display ]             |     |
  [ Reset Sensor & Shot Flags ]  |     |
               |                 |     |
               +---------->------+     |
                          |            |
                          v            v
                  +-------<------------+
                  |
                  v
           ( Loop to START )

===========================================================================


STEP-BY-STEP LOGIC EXECUTION:

1. INITIALIZATION
   - Set S_total = 0
   - Set netSensorState = CLEAR
   - Set isShotInFlight = FALSE
   - Set system timer t = 0

2. SHOT RELEASE DETECTION (Court Tracking)
   - Detect when a player releases a basketball toward the hoop.
   - Capture foot position at that exact instant:
     * Set shooterPosition = FREE_THROW, INSIDE_ARC, or OUTSIDE_ARC.
   - Set flag isShotInFlight = TRUE.

3. MAIN TIMING LOOP
   - Evaluate timer condition: Is t % 1 == 0?
     * NO  : Increment timer (t = t + 1) and return to Step 2.
     * YES : Proceed to Step 4 (Net Sensor Check).

4. GOAL & POINT EVALUATION
   - Read hardware state from the optical net sensor.
   - Evaluate condition: Is netSensorState == BROKEN?
     * NO  : Maintain current S_total value without making changes.
     * YES : If isShotInFlight == TRUE, determine point value:
             a. Evaluate shooterPosition:
                - IF FREE_THROW  -> points = 1
                - IF INSIDE_ARC  -> points = 2
                - IF OUTSIDE_ARC -> points = 3
             b. Increment total score: S_total = S_total + points
             c. Send update command to the digital scoreboard.
             d. Reset system flags:
                - netSensorState = CLEAR
                - isShotInFlight = FALSE

5. LOOP CONTINUATION
   - Return to Step 2 to continuously monitor the match.

================================================================================
