#!/usr/bin/env bash

Q_UI_FILE_PATH=~/dev/qtcreator/new_stock_robot/new_stock_robot


ROOTPATH=`pwd`;

echo $ROOTPATH
TARGET_PATH=$ROOTPATH


MainWindowUI_SRC=$Q_UI_FILE_PATH/captcha_collect_cli.ui
MainWindowUI_TARGET=$TARGET_PATH/MainWindowUI.py


pyside-uic $MainWindowUI_SRC -o $MainWindowUI_TARGET

echo From $MainWindowUI_SRC to $MainWindowUI_TARGET

echo done!