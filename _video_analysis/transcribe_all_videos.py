"""Legacy entry point for batch transcription.

This script now delegates to the dated-batch workflow in
`transcribe_batch2.py`, which reads the canonical video list from
`batch_config.py`.
"""

from transcribe_batch2 import main


if __name__ == "__main__":
    main()
