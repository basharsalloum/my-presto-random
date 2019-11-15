pipeline {
    agent any
        stages {
            stage("unit-test") {
                steps {
                    python -m pytest -v tests/test_my-random.py
                }
            }
        }
}
