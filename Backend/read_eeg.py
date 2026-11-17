import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
#Simple code for reading EEG data from a board using BrainFlow. This code initializes the board, 
#starts streaming data for 5 seconds, retrieves the data, and extracts EEG channels for further analysis.
#(untested code)
def main():
    # Enable BrainFlow logging for debugging
    BoardShim.enable_dev_board_logger()

    # Configure board parameters
    params = BrainFlowInputParams()

    # Select your Board ID
    board_id = BoardIds.SYNTHETIC_BOARD.value

    board = BoardShim(board_id, params)

    try:
        # Prepare the session and start streaming data for 5 seconds
        board.prepare_session()
        board.start_stream()
        print("Streaming raw data for 5 seconds...")
        time.sleep(5)

        # Get data from board
        data = board.get_board_data()

    finally:
        # stop streaming
        board.stop_stream()
        board.release_session()

    # extract EEG channels from the data
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    eeg_data = data[eeg_channels, :]

    print(f"Data shape (channels, samples): {eeg_data.shape}")
    print("First 5 samples of Channel 1 (uV):", eeg_data[0, :5])

if __name__ == "__main__":
    main()
