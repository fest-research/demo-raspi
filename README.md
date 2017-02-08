
### IOT Demo

Demo iot application that simulates a logistics packing desk


### Deploy to Kubernetes

Execute the following command against the Kubernetes API server. The demo application will be deployed automatically on all RaspberryPI devices

```shell
$ kubectl create -f https://raw.githubusercontent.com/fest-research/demo-raspi/master/assets/packing-daemonset.yaml
```

### Run from Source

SSH into the Raspberry. Run the follwoing commands

```shell
$ sudo apt-get update 
$ sudo apt-get install python python-dev python-rpi.gpio
$ python src/packingdesk.py 
```


### Travis

Travis CI [https://travis-ci.org/fest-research/demo-raspi]

