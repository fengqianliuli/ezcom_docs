
.. _program_listing_file_include_ezcom_client.h:

Program Listing for File client.h
=================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_client.h>` (``include/ezcom/client.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <functional>
   #include <memory>
   #include <string>
   
   #include "message.h"
   #include "node.h"
   
   namespace holosar {
   namespace ezcom {
   
   struct Result {
     ResultType res_type;
     std::shared_ptr<Message> rep_message;
   };
   
   using ConnectionCallback = std::function<void(const ConnectionEvent&)>;
   using ResultCallback = std::function<void(const Result)>;
   
   class Client : public Node {
    public:
     Client() = default;
     virtual ~Client() = default;
     virtual void Connect(const std::string& addr,
                          const ConnectionCallback& conn_cb = nullptr) = 0;
     virtual Result SyncRequest(const std::shared_ptr<Message>& req_message,
                                int timeout_ms = -1) = 0;
     virtual void AsyncRequest(const std::shared_ptr<Message>& req_message,
                               const ResultCallback& result_cb,
                               int timeout_ms = -1) = 0;
   };
   
   }  // namespace ezcom
   }  // namespace holosar
