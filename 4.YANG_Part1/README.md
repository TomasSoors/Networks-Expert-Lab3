# Part 7: Getting started with NETCONF/YANG – Part 1


## Preparation and Implementation

First start off with the reading this forum: https://community.cisco.com/t5/networking-blogs/getting-started-with-netconf-yang-part-1/ba-p/3661241

To make a connection you can use what we previously used to make a NETCONF connection through ssh, with the following command: 

`ssh -p 830 cisco@192.168.56.101`

and you will get the XML response of your router, which contains all the capabilities: 

![alt text](images/ssh.png)

to continue the session, you need to respond to the hello with a list of capabilities you wanna use. these capabilities represent what you can do through these requests and with the NETCONF session. 

we can just use the base to continue this session: 

```

<?xml version="1.0" encoding="UTF-8"?>

<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">

<capabilities>

  <capability>urn:ietf:params:netconf:base:1.0</capability>

</capabilities>

</hello>]]>]]>
```

with this combination `]]>]]>` indicating the end of the message. 
 

we can check the transport by trying a simple command which gives us the full running config of our router:

```

<?xml version="1.0"?>

<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"

message-id="101">

<get-config>

<source>

<running/>

</source>

</get-config>

</rpc>]]>]]>
```

with as a response: 

![alt text](images/device_config.png)


As for a NETCONF tool. we
## Troubleshooting

There were no real problems in this case, it was pretty straight forward and worked pretty seemlesly

## verification

