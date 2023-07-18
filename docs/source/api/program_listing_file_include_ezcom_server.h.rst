
.. _program_listing_file_include_ezcom_server.h:

Program Listing for File server.h
=================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_server.h>` (``include/ezcom/server.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <functional>
   #include <string>
   
   #include "message.h"
   #include "node.h"
   
   namespace holosar {
   namespace ezcom {
   
   using MessageHandler = std::function<const std::shared_ptr<Message>(
       const std::shared_ptr<Message>&)>;
   
   class Server : public Node {
    public:
     Server() = default;
     virtual ~Server() = default;
     virtual void Bind(const std::string& addr, const MessageHandler& handler) = 0;
   };
   
   }  // namespace ezcom
   }  // namespace holosar
