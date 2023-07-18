
.. _program_listing_file_include_ezcom_subscriber.h:

Program Listing for File subscriber.h
=====================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_subscriber.h>` (``include/ezcom/subscriber.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <functional>
   #include <string>
   
   #include "message.h"
   #include "node.h"
   
   namespace holosar {
   namespace ezcom {
   
   using MsgCallback = std::function<void(const std::shared_ptr<Message>&)>;
   
   class Subscriber : public Node {
    public:
     Subscriber() = default;
     virtual ~Subscriber() = default;
     virtual void Subscribe(const std::string& addr, const MsgCallback& msg_cb,
                            const std::string& topic = "default_topic") = 0;
   };
   
   }  // namespace ezcom
   }  // namespace holosar
