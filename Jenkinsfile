pipeline{
    agent any
    stages{
        stage("checkout SCM"){
            steps{
                git url: "https://github.com/gowtham123K/heamncy.git", branch:"main"
            }
        }
        stage("dependency"){
            steps{
                bat'''
                python -m venv venv 
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }
        stage("testing"){
            steps{
                bat '''
                call venv\\Scripts\\activate
                pytest test.py
                '''
            }
        }
        stage("deploy"){
            steps{
                bat '''
                call venv\\Scripts\\activate
                add.py
                '''
            }
        }
    }
}