# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.subprocess import PIPE
from ctypes import addressof
from typing import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import json
import requests
import threading



#shell process to launch leshan client 
p = 'None'   
class Ui_Widget(object):
    
    def setupUi(self, Widget):
            Widget.setObjectName("Widget")
            Widget.resize(932, 657)
            self.gridLayout_2 = QtWidgets.QGridLayout(Widget)
            self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
            self.gridLayout_2.setSpacing(5)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.currentDevice_display = QtWidgets.QLabel(Widget)
            self.currentDevice_display.setObjectName("currentDevice_display")
            self.gridLayout_2.addWidget(self.currentDevice_display, 3, 0, 1, 1)
            self.tabWidget = QtWidgets.QTabWidget(Widget)
            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.tabs = QtWidgets.QTabWidget(self.tab)
            self.tabs.setObjectName("tabs")
            self.tab_createIface = QtWidgets.QWidget()
            self.tab_createIface.setObjectName("tab_createIface")
            self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_createIface)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.CurrentDevice_label_display_Connexion = QtWidgets.QLabel(self.tab_createIface)
            self.CurrentDevice_label_display_Connexion.setObjectName("CurrentDevice_label_display_Connexion")
            self.gridLayout_3.addWidget(self.CurrentDevice_label_display_Connexion, 1, 0, 1, 1)
            self.scrollArea = QtWidgets.QScrollArea(self.tab_createIface)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
            self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 866, 447))
            self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
            self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
            self.gridLayout.setObjectName("gridLayout")
            self.createIface_inputDataSteam = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
            self.createIface_inputDataSteam.setObjectName("createIface_inputDataSteam")
            self.gridLayout.addWidget(self.createIface_inputDataSteam, 5, 1, 1, 1)
            self.createIface_inputPskId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
            self.createIface_inputPskId.setObjectName("createIface_inputPskId")
            self.gridLayout.addWidget(self.createIface_inputPskId, 3, 1, 1, 1)
            self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.label.setText("")
            self.label.setObjectName("label")
            self.gridLayout.addWidget(self.label, 3, 2, 1, 1)
            self.createIface_labelId = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.createIface_labelId.setObjectName("createIface_labelId")
            self.gridLayout.addWidget(self.createIface_labelId, 0, 0, 1, 1)
            self.createIface_inputId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
            self.createIface_inputId.setObjectName("createIface_inputId")
            self.gridLayout.addWidget(self.createIface_inputId, 0, 1, 1, 1)
            self.createIface_labelPsk = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.createIface_labelPsk.setObjectName("createIface_labelPsk")
            self.gridLayout.addWidget(self.createIface_labelPsk, 4, 0, 1, 1)
            self.createIface_labelDescription = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.createIface_labelDescription.setObjectName("createIface_labelDescription")
            self.gridLayout.addWidget(self.createIface_labelDescription, 1, 0, 1, 1)
            self.createIface_labelPskId = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.createIface_labelPskId.setObjectName("createIface_labelPskId")
            self.gridLayout.addWidget(self.createIface_labelPskId, 3, 0, 1, 1)
            self.createIface_inputDescription = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
            self.createIface_inputDescription.setObjectName("createIface_inputDescription")
            self.gridLayout.addWidget(self.createIface_inputDescription, 1, 1, 1, 1)
            self.createIface_labelDataStreamId = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
            self.createIface_labelDataStreamId.setObjectName("createIface_labelDataStreamId")
            self.gridLayout.addWidget(self.createIface_labelDataStreamId, 5, 0, 1, 1)
            self.createIface_inputPsk = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
            self.createIface_inputPsk.setObjectName("createIface_inputPsk")
            self.gridLayout.addWidget(self.createIface_inputPsk, 4, 1, 1, 1)
            self.createIface_validateButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
            self.createIface_validateButton.setObjectName("createIface_validateButton")
            self.gridLayout.addWidget(self.createIface_validateButton, 6, 0, 1, 3)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
            self.gridLayout_3.addWidget(self.scrollArea, 2, 0, 1, 1)
            self.CurrentDevice_label_Connexion = QtWidgets.QLabel(self.tab_createIface)
            self.CurrentDevice_label_Connexion.setObjectName("CurrentDevice_label_Connexion")
            self.gridLayout_3.addWidget(self.CurrentDevice_label_Connexion, 0, 0, 1, 1)
            self.tabs.addTab(self.tab_createIface, "")
            self.tab_connectClient = QtWidgets.QWidget()
            self.tab_connectClient.setObjectName("tab_connectClient")
            self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_connectClient)
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.connectClient_inputEndPointName = QtWidgets.QLineEdit(self.tab_connectClient)
            self.connectClient_inputEndPointName.setObjectName("connectClient_inputEndPointName")
            self.gridLayout_6.addWidget(self.connectClient_inputEndPointName, 0, 1, 1, 1)
            self.connectClient_validateButton = QtWidgets.QPushButton(self.tab_connectClient)
            self.connectClient_validateButton.setObjectName("connectClient_validateButton")
            self.gridLayout_6.addWidget(self.connectClient_validateButton, 3, 1, 1, 1)
            self.connectClient_inputPsk = QtWidgets.QLineEdit(self.tab_connectClient)
            self.connectClient_inputPsk.setObjectName("connectClient_inputPsk")
            self.gridLayout_6.addWidget(self.connectClient_inputPsk, 2, 1, 1, 1)
            self.connectClient_inputPskId = QtWidgets.QLineEdit(self.tab_connectClient)
            self.connectClient_inputPskId.setObjectName("connectClient_inputPskId")
            self.gridLayout_6.addWidget(self.connectClient_inputPskId, 1, 1, 1, 1)
            self.connectClient_labelEndPointName = QtWidgets.QLabel(self.tab_connectClient)
            self.connectClient_labelEndPointName.setObjectName("connectClient_labelEndPointName")
            self.gridLayout_6.addWidget(self.connectClient_labelEndPointName, 0, 0, 1, 1)
            self.connectClient_labelEndPointName_2 = QtWidgets.QLabel(self.tab_connectClient)
            self.connectClient_labelEndPointName_2.setObjectName("connectClient_labelEndPointName_2")
            self.gridLayout_6.addWidget(self.connectClient_labelEndPointName_2, 1, 0, 1, 1)
            self.connectClient_labelEndPointName_3 = QtWidgets.QLabel(self.tab_connectClient)
            self.connectClient_labelEndPointName_3.setObjectName("connectClient_labelEndPointName_3")
            self.gridLayout_6.addWidget(self.connectClient_labelEndPointName_3, 2, 0, 1, 1)
            self.tabs.addTab(self.tab_connectClient, "")
            self.tab_showResouces = QtWidgets.QWidget()
            self.tab_showResouces.setObjectName("tab_showResouces")
            self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_showResouces)
            self.gridLayout_7.setObjectName("gridLayout_7")
            self.showResources_validateButton = QtWidgets.QPushButton(self.tab_showResouces)
            self.showResources_validateButton.setObjectName("showResources_validateButton")
            self.gridLayout_7.addWidget(self.showResources_validateButton, 2, 1, 1, 1)
            self.showResources_InputId = QtWidgets.QLineEdit(self.tab_showResouces)
            self.showResources_InputId.setObjectName("showResources_InputId")
            self.gridLayout_7.addWidget(self.showResources_InputId, 0, 1, 1, 1)
            self.showResources_display = QtWidgets.QTextBrowser(self.tab_showResouces)
            self.showResources_display.setObjectName("showResources_display")
            self.gridLayout_7.addWidget(self.showResources_display, 1, 1, 1, 1)
            self.showResources_labelid = QtWidgets.QLabel(self.tab_showResouces)
            self.showResources_labelid.setObjectName("showResources_labelid")
            self.gridLayout_7.addWidget(self.showResources_labelid, 0, 0, 1, 1)
            self.tabs.addTab(self.tab_showResouces, "")
            self.tab_addResources = QtWidgets.QWidget()
            self.tab_addResources.setObjectName("tab_addResources")
            self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_addResources)
            self.gridLayout_8.setObjectName("gridLayout_8")
            self.label_12 = QtWidgets.QLabel(self.tab_addResources)
            self.label_12.setObjectName("label_12")
            self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)
            self.addResource_inputId = QtWidgets.QLineEdit(self.tab_addResources)
            self.addResource_inputId.setObjectName("addResource_inputId")
            self.gridLayout_8.addWidget(self.addResource_inputId, 0, 1, 1, 1)
            self.addResource_validatioButton = QtWidgets.QPushButton(self.tab_addResources)
            self.addResource_validatioButton.setObjectName("addResource_validatioButton")
            self.gridLayout_8.addWidget(self.addResource_validatioButton, 1, 0, 1, 2)
            self.tabs.addTab(self.tab_addResources, "")
            self.tab_connectedDevices = QtWidgets.QWidget()
            self.tab_connectedDevices.setObjectName("tab_connectedDevices")
            self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_connectedDevices)
            self.gridLayout_18.setObjectName("gridLayout_18")
            self.connectedDevices_display = QtWidgets.QTextBrowser(self.tab_connectedDevices)
            self.connectedDevices_display.setObjectName("connectedDevices_display")
            self.gridLayout_18.addWidget(self.connectedDevices_display, 1, 0, 1, 1)
            self.showConnectedDevices_validateButton = QtWidgets.QPushButton(self.tab_connectedDevices)
            self.showConnectedDevices_validateButton.setObjectName("showConnectedDevices_validateButton")
            self.gridLayout_18.addWidget(self.showConnectedDevices_validateButton, 0, 0, 1, 1)
            self.tabs.addTab(self.tab_connectedDevices, "")
            self.tab_deleteIface = QtWidgets.QWidget()
            self.tab_deleteIface.setObjectName("tab_deleteIface")
            self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_deleteIface)
            self.gridLayout_9.setObjectName("gridLayout_9")
            self.deleteInterface_labelId = QtWidgets.QLabel(self.tab_deleteIface)
            self.deleteInterface_labelId.setObjectName("deleteInterface_labelId")
            self.gridLayout_9.addWidget(self.deleteInterface_labelId, 0, 0, 1, 1)
            self.deleteInterface_inputId = QtWidgets.QLineEdit(self.tab_deleteIface)
            self.deleteInterface_inputId.setObjectName("deleteInterface_inputId")
            self.gridLayout_9.addWidget(self.deleteInterface_inputId, 0, 1, 1, 1)
            self.deleteInterface_validateButton = QtWidgets.QPushButton(self.tab_deleteIface)
            self.deleteInterface_validateButton.setObjectName("deleteInterface_validateButton")
            self.gridLayout_9.addWidget(self.deleteInterface_validateButton, 1, 1, 1, 1)
            self.tabs.addTab(self.tab_deleteIface, "")
            self.gridLayout_5.addWidget(self.tabs, 9, 0, 1, 1)
            self.tabWidget.addTab(self.tab, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
            self.scrollArea_2.setWidgetResizable(True)
            self.scrollArea_2.setObjectName("scrollArea_2")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 888, 542))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.gridLayout_17 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
            self.gridLayout_17.setObjectName("gridLayout_17")
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.gridLayout_17.addLayout(self.horizontalLayout, 1, 0, 1, 1)
            self.tabWidget_2 = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
            self.tabWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.tabWidget_2.setObjectName("tabWidget_2")
            self.tab_deviceInfos = QtWidgets.QWidget()
            self.tab_deviceInfos.setObjectName("tab_deviceInfos")
            self.tabWidget_2.addTab(self.tab_deviceInfos, "")
            self.tab_4 = QtWidgets.QWidget()
            self.tab_4.setObjectName("tab_4")
            self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_4)
            self.gridLayout_21.setObjectName("gridLayout_21")
            self.registeredOps_bodyInput = QtWidgets.QPlainTextEdit(self.tab_4)
            self.registeredOps_bodyInput.setPlainText("")
            self.registeredOps_bodyInput.setObjectName("registeredOps_bodyInput")
            self.gridLayout_21.addWidget(self.registeredOps_bodyInput, 4, 1, 1, 1)
            self.OpsRegisteredOps_idDeviceInput = QtWidgets.QLineEdit(self.tab_4)
            self.OpsRegisteredOps_idDeviceInput.setObjectName("OpsRegisteredOps_idDeviceInput")
            self.gridLayout_21.addWidget(self.OpsRegisteredOps_idDeviceInput, 1, 1, 1, 1)
            self.OpsRegisteredOps_idDevice = QtWidgets.QLabel(self.tab_4)
            self.OpsRegisteredOps_idDevice.setObjectName("OpsRegisteredOps_idDevice")
            self.gridLayout_21.addWidget(self.OpsRegisteredOps_idDevice, 1, 0, 1, 1)
            self.label_3 = QtWidgets.QLabel(self.tab_4)
            self.label_3.setObjectName("label_3")
            self.gridLayout_21.addWidget(self.label_3, 4, 0, 1, 1)
            self.registeredOps_display = QtWidgets.QTextBrowser(self.tab_4)
            self.registeredOps_display.setObjectName("registeredOps_display")
            self.gridLayout_21.addWidget(self.registeredOps_display, 5, 1, 1, 1)
            self.tabWidget_2.addTab(self.tab_4, "")
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_3)
            self.gridLayout_20.setObjectName("gridLayout_20")
            self.newOps_createNewOps = QtWidgets.QLabel(self.tab_3)
            self.newOps_createNewOps.setObjectName("newOps_createNewOps")
            self.gridLayout_20.addWidget(self.newOps_createNewOps, 0, 0, 1, 1)
            self.CreateNewOps_idDeviceInput = QtWidgets.QLineEdit(self.tab_3)
            self.CreateNewOps_idDeviceInput.setObjectName("CreateNewOps_idDeviceInput")
            self.gridLayout_20.addWidget(self.CreateNewOps_idDeviceInput, 0, 1, 1, 1)
            self.createNewOps_bodyInput = QtWidgets.QTextEdit(self.tab_3)
            self.createNewOps_bodyInput.setObjectName("createNewOps_bodyInput")
            self.gridLayout_20.addWidget(self.createNewOps_bodyInput, 1, 1, 1, 1)
            self.createNewOps_display = QtWidgets.QTextBrowser(self.tab_3)
            self.createNewOps_display.setObjectName("createNewOps_display")
            self.gridLayout_20.addWidget(self.createNewOps_display, 2, 1, 1, 1)
            self.newOps_Body = QtWidgets.QLabel(self.tab_3)
            self.newOps_Body.setObjectName("newOps_Body")
            self.gridLayout_20.addWidget(self.newOps_Body, 1, 0, 1, 1)
            self.tabWidget_2.addTab(self.tab_3, "")
            self.tab_5 = QtWidgets.QWidget()
            self.tab_5.setObjectName("tab_5")
            self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_5)
            self.gridLayout_19.setObjectName("gridLayout_19")
            self.RWX_bodyInput_2 = QtWidgets.QTextEdit(self.tab_5)
            self.RWX_bodyInput_2.setObjectName("RWX_bodyInput_2")
            self.gridLayout_19.addWidget(self.RWX_bodyInput_2, 2, 1, 1, 1)
            self.RWX_labelBody = QtWidgets.QLabel(self.tab_5)
            self.RWX_labelBody.setObjectName("RWX_labelBody")
            self.gridLayout_19.addWidget(self.RWX_labelBody, 2, 0, 1, 1)
            self.Read_idLabel = QtWidgets.QLabel(self.tab_5)
            self.Read_idLabel.setObjectName("Read_idLabel")
            self.gridLayout_19.addWidget(self.Read_idLabel, 1, 0, 1, 1)
            self.RWX_display = QtWidgets.QTextBrowser(self.tab_5)
            self.RWX_display.setObjectName("RWX_display")
            self.gridLayout_19.addWidget(self.RWX_display, 3, 1, 1, 1)
            self.OpsRead_idDeviceInput = QtWidgets.QLineEdit(self.tab_5)
            self.OpsRead_idDeviceInput.setObjectName("OpsRead_idDeviceInput")
            self.gridLayout_19.addWidget(self.OpsRead_idDeviceInput, 1, 1, 1, 1)
            self.tabWidget_2.addTab(self.tab_5, "")
            self.gridLayout_17.addWidget(self.tabWidget_2, 0, 0, 1, 1)
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
            self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
            self.tabWidget.addTab(self.tab_2, "")
            self.gridLayout_2.addWidget(self.tabWidget, 9, 0, 1, 1)
            self.CurrentDevic_label = QtWidgets.QLabel(Widget)
            self.CurrentDevic_label.setObjectName("CurrentDevic_label")
            self.gridLayout_2.addWidget(self.CurrentDevic_label, 2, 0, 1, 1)

            #linking buttons to functions

            self.createIface_validateButton.clicked.connect(self.createIface_function)
            self.deleteInterface_validateButton.clicked.connect(self.deleteIface_function)
            self.connectClient_validateButton.clicked.connect(self.connectIface_function)
            self.showResources_validateButton.clicked.connect(self.showResources_function)
            self.addResource_validatioButton.clicked.connect(self.addResoource_function)
            self.showConnectedDevices_validateButton.clicked.connect(self.showConnectedDevices_function)

            self.retranslateUi(Widget)
            self.tabWidget.setCurrentIndex(0)
            self.tabs.setCurrentIndex(4)
            self.tabWidget_2.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Widget)
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.currentDevice_display.setText(_translate("Widget", "TextLabel"))
        self.CurrentDevice_label_display_Connexion.setText(_translate("Widget", "TextLabel"))
        self.createIface_labelId.setText(_translate("Widget", "Id"))
        self.createIface_labelPsk.setText(_translate("Widget", "PSK"))
        self.createIface_labelDescription.setText(_translate("Widget", "Description"))
        self.createIface_labelPskId.setText(_translate("Widget", "PSK Id"))
        self.createIface_labelDataStreamId.setText(_translate("Widget", "Data Stream Id"))
        self.createIface_validateButton.setText(_translate("Widget", "Create"))
        self.CurrentDevice_label_Connexion.setText(_translate("Widget", "Current Device"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_createIface), _translate("Widget", "Create interface"))
        self.connectClient_validateButton.setText(_translate("Widget", "Connect"))
        self.connectClient_labelEndPointName.setText(_translate("Widget", "Endpoint "))
        self.connectClient_labelEndPointName_2.setText(_translate("Widget", "PSK Id"))
        self.connectClient_labelEndPointName_3.setText(_translate("Widget", "PSK"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_connectClient), _translate("Widget", "Connect client"))
        self.showResources_validateButton.setText(_translate("Widget", "Show resources"))
        self.showResources_labelid.setText(_translate("Widget", "Id"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_showResouces), _translate("Widget", "Show Resources"))
        self.label_12.setText(_translate("Widget", "Resource Id"))
        self.addResource_validatioButton.setText(_translate("Widget", "Add"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_addResources), _translate("Widget", "Add resources"))
        self.showConnectedDevices_validateButton.setText(_translate("Widget", "Show connected devices"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_connectedDevices), _translate("Widget", "Connected devices"))
        self.deleteInterface_labelId.setText(_translate("Widget", "Id"))
        self.deleteInterface_validateButton.setText(_translate("Widget", "Delete"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_deleteIface), _translate("Widget", "Delete interface"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Connexion"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_deviceInfos), _translate("Widget", "Device resources"))
        self.OpsRegisteredOps_idDevice.setText(_translate("Widget", "Device"))
        self.label_3.setText(_translate("Widget", "Body"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Widget", "Registered Operations"))
        self.newOps_createNewOps.setText(_translate("Widget", "Device"))
        self.createNewOps_bodyInput.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{&quot;type&quot;:&quot;READ&quot;,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;paths&quot;:[&quot;/5/0&quot;]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p></body></html>"))
        self.newOps_Body.setText(_translate("Widget", "Body"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Widget", "Create a new operation"))
        self.RWX_labelBody.setText(_translate("Widget", "Body"))
        self.Read_idLabel.setText(_translate("Widget", "Device"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Widget", "Read/Write/Execute"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "Operations"))
        self.CurrentDevic_label.setText(_translate("Widget", "Current Device"))
    
    
        def createIface_function(self):
                
                        global ifaceNumber
                        url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices"

                        payload = {
                                "id": "urn:lo:nsid:lwm2m:"+ self.createIface_inputId.text(),
                                "name": "Lwm2m device",
                                "description": "device for test",
                                "defaultDataStreamId": "urn:lo:nsid:lwm2m:ifacelwm2m",
                                "interfaces": [
                                    {
                                        "connector": "lwm2m",
                                        "enabled": "true",
                                        "definition": {
                                            "endpointName": "balbla",
                                            "security": {
                                                "pskInfo": {
                                                    "identity": "pskId",
                                                    "secret" : "6d7973656372657470736b617a657274"
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        

                        payload['name'] = self.createIface_inputId.text()
                        payload['description'] = self.createIface_inputDescription.text()
        
                        payload['interfaces'][0]['definition']['endpointName'] = "urn:lo:lwm2m:"+ self.createIface_inputId.text()
                        payload['interfaces'][0]['definition']['security']['pskInfo']['identity'] = self.createIface_inputId.text()

                        payload = json.dumps(payload)
                        
                        headers = {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                            'X-API-Key': '1d576207727841a7b9aa2a1f24448f86',
                            'Cookie': 'XSRF-TOKEN=d4af0d8c-5e37-415f-8c72-3da0a7f68c5c'
                        }
                        response = requests.request("POST", url, headers=headers, data=payload,verify =False)
                        print(response.text)
    def createIface_function(self):
        
                global ifaceNumber
                url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices"

                payload = {
                        "id": "urn:lo:nsid:lwm2m:"+ self.createIface_inputId.text(),
                        "name": "Lwm2m device",
                        "description": "device for test",
                        "defaultDataStreamId": "urn:lo:nsid:lwm2m:ifacelwm2m",
                        "interfaces": [
                            {
                                "connector": "lwm2m",
                                "enabled": "true",
                                "definition": {
                                    "endpointName": "balbla",
                                    "security": {
                                        "pskInfo": {
                                            "identity": "pskId",
                                            "secret" : "6d7973656372657470736b617a657274"
                                        }
                                    }
                                }
                            }
                        ]
                    }
                

                payload['name'] = self.createIface_inputId.text()
                payload['description'] = self.createIface_inputDescription.text()
 
                payload['interfaces'][0]['definition']['endpointName'] = "urn:lo:lwm2m:"+ self.createIface_inputId.text()
                payload['interfaces'][0]['definition']['security']['pskInfo']['identity'] = self.createIface_inputId.text()

                payload = json.dumps(payload)
                
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-API-Key': '1d576207727841a7b9aa2a1f24448f86',
                    'Cookie': 'XSRF-TOKEN=d4af0d8c-5e37-415f-8c72-3da0a7f68c5c'
                }
                response = requests.request("POST", url, headers=headers, data=payload,verify =False)
                print(response.text)
    def connectIface_function(self):
        global p 
        if (p =='None'):
            urn = "java -jar leshan-client-demo.jar "+ "-n "+ "urn:lo:lwm2m:"+ self.connectClient_inputEndPointName.text() +" -i "+ self.connectClient_inputEndPointName.text()+" -p 6d7973656372657470736b617a657274 -u lwm2m.integ.m2m.orange.com"
            urn = urn.strip('"')
            p = subprocess.Popen(["java","-jar","leshan-client-demo.jar","-n","urn:lo:lwm2m:"+self.connectClient_inputEndPointName.text(),"-i",self.connectClient_inputEndPointName.text(),"-p","6d7973656372657470736b617a657274","-u","lwm2m.integ.m2m.orange.com"], stdin=PIPE,stderr=PIPE)
        else:
            print("p has already been changed")
    def deleteIface_function(self):
            url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:"+ self.connectClient_inputEndPointName.text()
            payload={}
            headers = {
            'X-API-Key': '1d576207727841a7b9aa2a1f24448f86'
                    }

            response = requests.request("DELETE", url, headers=headers, data=payload,verify =False)
    def showResources_function(self):
        url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:"+self.showResources_InputId.text() +"/twin/supported-objects"
        payload={}
        headers = {
            'X-API-Key': '1d576207727841a7b9aa2a1f24448f86',
            'Cookie': 'XSRF-TOKEN=6247a9f8-7cab-47b4-9706-1df68f174806'
                }

        response = requests.request("GET", url, headers=headers, data=payload,verify = False)

        print(response.text)
        self.showResources_display.setText(response.text)    
    def addResoource_function(self): 
        
        def addResource_thread():
            global p
            strCreate = "create " + self.addResource_inputId.text()+'\n' #"create 3424"
            p.stdin.write(bytes(strCreate,encoding='utf8'))
            p.stdin.flush()
        t2 = threading.Thread(target=addResource_thread)
        t2.start()
        
    def showConnectedDevices_function(self):
        
        
        #Registered devices
        url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices"
        payload={}
        headers = {'X-API-Key': '1d576207727841a7b9aa2a1f24448f86'}
        response = requests.request("GET", url, headers=headers, data=payload,verify =False).text
        response = json.loads(response)
        
        registreredDevices = []

        for element in range(len(response)):
            registreredDevices.append(response[element]['id'])
            registreredDevices[element]=registreredDevices[element].replace("urn:lo:nsid:lwm2m:","")
        print(registreredDevices)
   
        
        connectedDevices = []
        device_info = []
        url_devices = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:"
        
        payload = ""
        headers = {'X-API-Key': '1d576207727841a7b9aa2a1f24448f86','Content-Type': 'application/json'}
        
        
        
        for urn in range(len(registreredDevices)):
            response = requests.request("GET", url_devices+registreredDevices[urn], headers=headers, data=payload,verify=False).text
            response = json.loads(response)
            if(response['interfaces'][0]['status'] == 'ONLINE'):
                connectedDevices.append("Device  " + registreredDevices[urn])
        print(connectedDevices)
        
        #join list elements for display
        
        self.connectedDevices_display.setText('\n'.join(connectedDevices))
        
            
            #connectedDevices.append(registreredDevices[urn])
         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
