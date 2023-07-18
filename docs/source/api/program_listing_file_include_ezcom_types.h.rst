
.. _program_listing_file_include_ezcom_types.h:

Program Listing for File types.h
================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_types.h>` (``include/ezcom/types.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   namespace holosar {
   namespace ezcom {
   
   constexpr int kZmqRcvTimeout = 1000;
   constexpr int kZmqSndTimeout = 1000;
   
   enum class NodeType {
     kClient = 0,
     kServer = 1,
     kPublisher = 2,
     kSubscriber = 3,
   };
   
   enum class CommMode {
     kReqRep = 0,
     kPubSub = 1,
   };
   
   enum class TransportType {
     kZmqInproc = 0,
     kZmqIpc = 1,
     kZmqTcp = 2,
   };
   
   enum class ConnectionEvent {
     kConnected = 0,
     kDisconnected = 1,
   };
   
   enum class ResultType {
     kSuccess = 0,
     kTimeout = 1,
     kCommError = 2,
     kInvaildParam = 3,
     kUnknownError = 4,
   };
   
   }  // namespace ezcom
   }  // namespace holosar
